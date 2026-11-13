import {PNG} from 'pngjs';
import pixelmatch from 'pixelmatch';
import fs from 'node:fs/promises';
import path from 'node:path';

function bounded(value,name,min=0,max=1){if(!Number.isFinite(value)||value<min||value>max)throw Error(`Invalid ${name}`);return value;}
function crop(p,r){const out=new PNG({width:r.width,height:r.height});PNG.bitblt(p,out,r.x,r.y,r.width,r.height,0,0);return out;}
export function compareLayout(reference,actual,maxAnchorError=2){
 bounded(maxAnchorError,'maxAnchorError',0,10000);
 if(reference.viewport?.width!==actual.viewport?.width||reference.viewport?.height!==actual.viewport?.height)throw Error('Layout viewport mismatch');
 for(const capture of [reference,actual]){const names=(capture.regions??[]).map(r=>r.name);if(names.some(n=>typeof n!=='string'||!n.trim())||new Set(names).size!==names.length)throw Error('Invalid or duplicate layout region names');}
 const regions=(reference.regions??[]).map(r=>{const other=(actual.regions??[]).find(x=>x.name===r.name);
  if(r.missing||!r.rect||!other?.rect||other.missing||r.rect.width<=0||r.rect.height<=0||other.rect.width<=0||other.rect.height<=0)return {name:r.name,pass:false,reason:'missing or non-measurable region'};
  const errors=Object.fromEntries(['x','y','width','height'].map(k=>[k,Math.abs(r.rect[k]-other.rect[k])]));
  const linesMatch=Number.isInteger(r.lines)&&r.lines===other.lines;
  return {name:r.name,errors,linesMatch,pass:linesMatch&&Object.values(errors).every(v=>Number.isFinite(v)&&v<=maxAnchorError)};
 });return {maxAnchorError,regions,pass:regions.length>0&&regions.every(r=>r.pass)};
}
export function compareImages(a,b,options={}){
 if(a.width!==b.width||a.height!==b.height)throw Error('Image dimensions differ; explicit reference-scale calibration required');
 const threshold=bounded(options.threshold??0.1,'threshold'),maxRatio=bounded(options.maxDiffRatio??0.01,'maxDiffRatio');
 const includeAA=options.includeAA??false;
 function metric(x,y){const diff=new PNG({width:x.width,height:x.height});const count=pixelmatch(x.data,y.data,diff.data,x.width,x.height,{threshold,includeAA});let raw=0;for(let i=0;i<x.data.length;i+=4){if(x.data.subarray(i,i+4).some((v,j)=>v!==y.data[i+j]))raw++;}return {count,ratio:count/(x.width*x.height),rawDifferentPixels:raw,pass:count/(x.width*x.height)<=maxRatio,diff};}
 const page=metric(a,b),names=new Set();
 const regions=(options.regions??[]).map(r=>{
  if(!r.name||names.has(r.name)||![r.x,r.y,r.width,r.height].every(Number.isInteger)||r.x<0||r.y<0||r.width<=0||r.height<=0||r.x+r.width>a.width||r.y+r.height>a.height)throw Error('Invalid or duplicate region');names.add(r.name);
  const {diff,...result}=metric(crop(a,r),crop(b,r));return {name:r.name,...result};
 });
 const overlay=new PNG({width:a.width,height:a.height});for(let i=0;i<a.data.length;i++)overlay.data[i]=Math.round((a.data[i]+b.data[i])/2);
 const {diff,...pageResult}=page;
 return {schemaVersion:1,dimensions:{width:a.width,height:a.height},settings:{threshold,maxDiffRatio:maxRatio,includeAA},exact:page.rawDifferentPixels===0,withinTolerance:page.pass&&regions.every(r=>r.pass),page:pageResult,regions,diff,overlay};
}
export async function compareFiles(reference,actual,out,options={}){
 const normalize=p=>process.platform==='win32'?path.resolve(p).toLowerCase():path.resolve(p);
 const inputPaths=await Promise.all([reference,actual].map(p=>fs.realpath(p)));
 const inputs=inputPaths.map(normalize),inputStats=await Promise.all(inputPaths.map(p=>fs.stat(p)));
 await fs.mkdir(out,{recursive:true});const realOut=await fs.realpath(out);
 for(const name of ['reference.png','actual.png','diff.png','overlay.png','comparison.json','report.html']){
  let dest=path.join(realOut,name),stat;try{dest=await fs.realpath(dest);stat=await fs.stat(dest);}catch(e){if(e.code!=='ENOENT')throw e;}
  if(inputs.includes(normalize(dest))||(stat&&inputStats.some(s=>s.ino===stat.ino&&s.dev===stat.dev)))throw Error('Comparison output would overwrite an input; use a separate output directory');
 }
 const a=PNG.sync.read(await fs.readFile(reference)),b=PNG.sync.read(await fs.readFile(actual));
 const {diff,overlay,...result}=compareImages(a,b,options);await fs.mkdir(out,{recursive:true});
 await fs.copyFile(reference,path.join(out,'reference.png'));await fs.copyFile(actual,path.join(out,'actual.png'));
 await fs.writeFile(path.join(out,'diff.png'),PNG.sync.write(diff));await fs.writeFile(path.join(out,'overlay.png'),PNG.sync.write(overlay));
 await fs.writeFile(path.join(out,'comparison.json'),JSON.stringify({...result,reference,actual},null,2));return result;
}

#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {capturePage} from './browser.mjs';
import {compareFiles,compareLayout} from './compare.mjs';
import {writeReport} from './report.mjs';

const usage='pixelclone collect|capture|fonts|compare|report --config config.json --out directory';
const [command,...args]=process.argv.slice(2),opts={};
try{
 if(command==='--help'||!command){console.log(usage);process.exit(0);}
 for(let i=0;i<args.length;i+=2){if(!args[i].startsWith('--')||args[i+1]===undefined||args[i+1].startsWith('--'))throw Error(`Expected --key value: ${args[i]}`);opts[args[i].slice(2)]=args[i+1];}
 const config=opts.config?JSON.parse(await fs.readFile(opts.config,'utf8')):{};
 const out=path.resolve(opts.out??'pixelclone-result');
 let result;
 const python=(mode,src)=>{
  if(!src)throw Error('Missing --src');
  const script=path.join(path.dirname(fileURLToPath(import.meta.url)),'python','inspect_reference.py');
  const r=spawnSync(opts.python??process.env.PIXELCLONE_PYTHON??'python',[script,mode,'--src',src,'--out',out,...(opts.text?['--text',opts.text]:[]),...(opts.fps?['--fps',opts.fps]:[])],{encoding:'utf8'});
  if(r.error)throw Error(`Python unavailable: ${r.error.message}. Set PIXELCLONE_PYTHON.`);
  if(r.status!==0)throw Error(r.stderr||r.stdout);return JSON.parse(r.stdout);
 };
 switch(command){
  case 'collect':
   if(opts.type==='image'||opts.type==='video')result=python(opts.type,opts.src);
   else result=await capturePage({...config,url:opts.url??config.url},out);
   break;
  case 'capture':result=await capturePage({...config,url:opts.url??config.url},out);break;
  case 'fonts':result=opts.src?python('fonts',opts.src):await capturePage({...config,url:opts.url??config.url},out);break;
  case 'compare':
   if(!opts.reference||!opts.actual)throw Error('compare requires --reference and --actual PNG paths');
   result=await compareFiles(opts.reference,opts.actual,out,config);
   if(opts['reference-capture']||opts['actual-capture']){
    if(!opts['reference-capture']||!opts['actual-capture'])throw Error('Supply both --reference-capture and --actual-capture');
    result.layout=compareLayout(JSON.parse(await fs.readFile(opts['reference-capture'],'utf8')),JSON.parse(await fs.readFile(opts['actual-capture'],'utf8')),config.maxAnchorError??2);
    await fs.writeFile(path.join(out,'comparison.json'),JSON.stringify(result,null,2));
   }
   await writeReport(out);if(!result.withinTolerance||result.layout?.pass===false)process.exitCode=2;break;
  case 'report':result=await writeReport(out);break;
  default:throw Error(usage);
 }
 console.log(JSON.stringify(result,null,2));
}catch(error){console.error(error.message);process.exitCode=1;}

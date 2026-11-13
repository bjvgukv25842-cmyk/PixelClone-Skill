import {chromium} from 'playwright';
import fs from 'node:fs/promises';
const out='work/round-1/source';await fs.mkdir(out,{recursive:true});
const browser=await chromium.launch({channel:'msedge',headless:true});
try{
const page=await browser.newPage({viewport:{width:1440,height:900}});
await page.addInitScript(()=>{window.__probe={shaders:[],contexts:[]};const orig=HTMLCanvasElement.prototype.getContext;HTMLCanvasElement.prototype.getContext=function(type,...args){const gl=orig.call(this,type,...args);if(gl&&!window.__probe.contexts.includes(type))window.__probe.contexts.push(type);return gl;};for(const Type of [window.WebGLRenderingContext,window.WebGL2RenderingContext].filter(Boolean)){const orig=Type.prototype.shaderSource;Type.prototype.shaderSource=function(shader,source){window.__probe.shaders.push({type:this.getShaderParameter(shader,this.SHADER_TYPE),source});return orig.call(this,shader,source);};}});
const downloads=[];let seq=0;
page.on('response',r=>{if(['script','stylesheet'].includes(r.request().resourceType())){const i=seq++;downloads.push(r.body().then(async b=>{const file=`asset-${i}.${r.request().resourceType()==='script'?'js':'css'}`;await fs.writeFile(out+'/'+file,b);return {url:r.url(),file};}).catch(e=>({url:r.url(),error:e.message})));}});
await page.goto('https://monopo.london/',{waitUntil:'domcontentloaded',timeout:60000});await page.waitForTimeout(10000);
await fs.writeFile(out+'/probe.json',JSON.stringify(await page.evaluate(()=>window.__probe),null,2));
await fs.writeFile(out+'/dom.html',await page.content());await fs.writeFile(out+'/sources.json',JSON.stringify(await Promise.all(downloads),null,2));
await page.screenshot({path:out+'/desktop.png'});console.log(await page.evaluate(()=>({contexts:window.__probe.contexts,shaders:window.__probe.shaders.length,scripts:[...document.scripts].map(x=>x.src)})));
}finally{await browser.close();}

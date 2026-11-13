import test from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import {mkdtemp,readFile} from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {capturePage} from '../toolkit/browser.mjs';
import {spawnSync} from 'node:child_process';
import {PNG} from 'pngjs';

test('capture records overflow, missing images, text layout and changed interaction state',async()=>{
 const server=http.createServer((req,res)=>{if(req.url==='/missing.png'){res.writeHead(404);res.end();return;}res.end('<html><body style="width:1500px"><h1>Hello</h1><img src="/missing.png"><button onclick="document.querySelector(\'h1\').textContent=\'Opened\'">Open</button></body></html>');});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 try{
 const out=await mkdtemp(path.join(os.tmpdir(),'pixelclone-'));
 const result=await capturePage({url:`http://127.0.0.1:${server.address().port}`,viewport:{width:800,height:600},regions:[{name:'title',selector:'h1'}],actions:[{type:'click',selector:'button'}]},out);
 assert.equal(result.regions[0].text,'Opened');assert.equal(result.overflow,true);assert.equal(result.images[0].loaded,false);
 assert.equal(result.regions[0].lines,1); assert.ok(result.browserVersion);assert.ok((await readFile(path.join(out,'screenshot.png'))).length>100);
 }finally{server.close();}
});
test('non-settling motion adapter times out instead of hanging',{timeout:3000},async()=>{
 const server=http.createServer((req,res)=>res.end('<script>window.__pixelclone={ready:new Promise(()=>{}),setState(){}}</script>'));
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 try{await assert.rejects(capturePage({url:`http://127.0.0.1:${server.address().port}`,state:{progress:0.5},timeoutMs:500},await mkdtemp(path.join(os.tmpdir(),'pixelclone-adapter-'))),/adapter|Timeout/i);}finally{server.close();}
});
test('static capture measures the same settled animation state as screenshot',async()=>{
 const server=http.createServer((req,res)=>res.end('<style>@keyframes slide{from{margin-left:0}to{margin-left:200px}}h1{animation:slide 10s linear forwards}</style><h1>Hi</h1>'));
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 try{const result=await capturePage({url:`http://127.0.0.1:${server.address().port}`,animationMode:'static',regions:[{name:'title',selector:'h1'}]},await mkdtemp(path.join(os.tmpdir(),'pixelclone-static-')));assert.ok(Math.abs(result.regions[0].rect.x-208)<1,JSON.stringify(result.regions[0].rect));}finally{server.close();}
});
test('invalid context configuration exits without leaking a browser',()=>{
 const child=spawnSync(process.execPath,['--input-type=module','-e',"import {capturePage} from './toolkit/browser.mjs'; capturePage({url:'http://localhost:1',colorScheme:'invalid'},'work/invalid-context-test').catch(()=>process.exitCode=1)"],{encoding:'utf8',timeout:5000});assert.equal(child.status,1,child.error?.message);
});
test('capture waits for CSS background loaded by an interaction',async()=>{
 let served=false;const png=new PNG({width:2,height:2});png.data.fill(200);
 const server=http.createServer((req,res)=>{if(req.url==='/slow.png'){setTimeout(()=>{res.setHeader('Content-Type','image/png');res.end(PNG.sync.write(png));served=true;},700);return;}res.end('<button onclick="document.body.style.backgroundImage=\'url(/slow.png)\'">Load</button>');});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 try{await capturePage({url:`http://127.0.0.1:${server.address().port}`,actions:[{type:'click',selector:'button'}]},await mkdtemp(path.join(os.tmpdir(),'pixelclone-bg-')));assert.equal(served,true);}finally{server.close();}
});

test('opt-in render audit distinguishes canvas text and GPU shader evidence from DOM fonts',async()=>{
 const server=http.createServer((req,res)=>res.end(`<!doctype html><canvas id="text"></canvas><canvas id="gpu"></canvas><h1 style="font-size:0">Visible in canvas</h1><script>
 console.error('Renderer shader failed without throwing');const c=document.querySelector('#text').getContext('2d');c.font='24px serif';c.fillText('Raster title',4,40);for(let i=0;i<120;i++)c.fillText('Sample '+i,4,100);
 let conversions=0;c.fillText({toString(){if(++conversions>1)throw Error('coerced twice');return 'Object-valued text';}},0,0);
 const gl=document.querySelector('#gpu').getContext('webgl');if(gl){const s=gl.createShader(gl.FRAGMENT_SHADER);gl.shaderSource(s,'precision mediump float; uniform sampler2D mapSampler; void main(){gl_FragColor=vec4(1.0);}');gl.compileShader(s);}
 </script>`));
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 try{const result=await capturePage({url:`http://127.0.0.1:${server.address().port}`,renderAudit:true},await mkdtemp(path.join(os.tmpdir(),'pixelclone-render-')));
 assert.ok(result.renderAudit,'render audit missing');
 assert.ok(result.renderAudit.contexts.some(c=>c.type==='2d'));
 assert.ok(result.renderAudit.contexts.some(c=>c.type==='webgl'));
 assert.equal(result.renderAudit.textDraws[0].text,'Raster title');
 assert.equal(result.renderAudit.textDraws[0].font,'24px serif');
 assert.equal(result.renderAudit.textDraws.length,100);assert.equal(result.renderAudit.truncated,true);
 assert.ok(result.renderAudit.shaders.some(s=>s.source.includes('mapSampler')&&s.sha256.length===64));
 assert.equal(result.renderAudit.isFidelityProof,false);
 assert.ok(result.consoleErrors?.some(e=>e.text==='Renderer shader failed without throwing'));
 assert.deepEqual(result.errors,[],'observing text must not introduce exceptions');
 }finally{server.close();}
});

test('mobile capture honors touch input instead of only shrinking desktop viewport',async()=>{
 const server=http.createServer((req,res)=>res.end('<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1"><h1></h1><script>document.querySelector("h1").textContent=matchMedia("(pointer: coarse)").matches?"touch":"mouse"</script>'));
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 try{const result=await capturePage({url:`http://127.0.0.1:${server.address().port}`,viewport:{width:390,height:844},hasTouch:true,isMobile:true,regions:[{name:'input-mode',selector:'h1'}]},await mkdtemp(path.join(os.tmpdir(),'pixelclone-touch-')));assert.equal(result.regions[0].text,'touch');}finally{server.close();}
});


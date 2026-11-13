import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {PNG} from 'pngjs';
test('CLI compare writes an offline report and uses failure exit code',async()=>{
 const dir=await fs.mkdtemp(path.join(os.tmpdir(),'pixelclone-cli-'));const a=new PNG({width:4,height:4});a.data.fill(255);await fs.writeFile(path.join(dir,'a.png'),PNG.sync.write(a));a.data.fill(0);await fs.writeFile(path.join(dir,'b.png'),PNG.sync.write(a));
 const r=spawnSync(process.execPath,['toolkit/pixelclone.mjs','compare','--reference',path.join(dir,'a.png'),'--actual',path.join(dir,'b.png'),'--out',path.join(dir,'result')],{encoding:'utf8'});
 assert.equal(r.status,2,r.stderr);assert.ok((await fs.readFile(path.join(dir,'result','report.html'),'utf8')).includes('diff.png'));
});
test('CLI unknown command fails with actionable help',()=>{
 const r=spawnSync(process.execPath,['toolkit/pixelclone.mjs','unknown'],{encoding:'utf8'});assert.equal(r.status,1);assert.match(r.stderr,/collect.*capture.*fonts.*compare.*report/);
});
test('comparison output cannot overwrite an input',async()=>{
 const dir=await fs.mkdtemp(path.join(os.tmpdir(),'pixelclone-source-'));const a=new PNG({width:4,height:4});a.data.fill(255);const bytes=PNG.sync.write(a);await fs.writeFile(path.join(dir,'reference.png'),bytes);a.data.fill(0);await fs.writeFile(path.join(dir,'b.png'),PNG.sync.write(a));
 const r=spawnSync(process.execPath,['toolkit/pixelclone.mjs','compare','--reference',path.join(dir,'b.png'),'--actual',path.join(dir,'reference.png'),'--out',dir],{encoding:'utf8'});
 assert.equal(r.status,1);assert.deepEqual(await fs.readFile(path.join(dir,'reference.png')),bytes);
});
test('linked output directory cannot alias a reference',async()=>{
 const dir=await fs.mkdtemp(path.join(os.tmpdir(),'pixelclone-alias-'));const real=path.join(dir,'real');await fs.mkdir(real);const alias=path.join(dir,'alias');await fs.symlink(real,alias,process.platform==='win32'?'junction':'dir');
 const a=new PNG({width:4,height:4});a.data.fill(255);const bytes=PNG.sync.write(a);await fs.writeFile(path.join(real,'diff.png'),bytes);a.data.fill(0);await fs.writeFile(path.join(real,'b.png'),PNG.sync.write(a));
 const r=spawnSync(process.execPath,['toolkit/pixelclone.mjs','compare','--reference',path.join(real,'diff.png'),'--actual',path.join(real,'b.png'),'--out',alias],{encoding:'utf8'});
 assert.equal(r.status,1);assert.deepEqual(await fs.readFile(path.join(real,'diff.png')),bytes);
});

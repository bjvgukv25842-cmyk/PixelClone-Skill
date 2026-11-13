import {chromium} from 'playwright';import fs from 'node:fs/promises';
const out='../outputs/pixelclone-review/round-1';const browser=await chromium.launch({channel:'msedge',headless:true});
try{for(const [label,url] of [['reference','https://monopo.london/'],['candidate','http://127.0.0.1:8765/round-1/candidate/index.html']]){
 if(process.argv[2]&&process.argv[2]!==label)continue;const folder=out+'/'+label+'/recording';await fs.mkdir(folder,{recursive:true});const context=await browser.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1});const page=await context.newPage();await page.goto(url,{waitUntil:'domcontentloaded',timeout:60000});await page.waitForTimeout(8000);
 const cdp=await context.newCDPSession(page),frames=[],writes=[],actions=[];let count=0;
 cdp.on('Page.screencastFrame',event=>{const index=count++,file='frame-'+String(index).padStart(4,'0')+'.jpg';frames.push({index,file,timestamp:event.metadata.timestamp,metadata:event.metadata});writes.push(fs.writeFile(folder+'/'+file,Buffer.from(event.data,'base64')));cdp.send('Page.screencastFrameAck',{sessionId:event.sessionId}).catch(()=>{});});
 await cdp.send('Page.startScreencast',{format:'jpeg',quality:92,maxWidth:1440,maxHeight:900,everyNthFrame:1});const start=Date.now();
 await page.waitForTimeout(500);
 for(let i=0;i<=48;i++){const t=i/48,x=720+400*Math.sin(t*Math.PI*2),y=450-150*Math.sin(t*Math.PI*4);await page.mouse.move(x,y);actions.push({elapsedMs:Date.now()-start,pointer:{x,y}});await page.waitForTimeout(65);}
 await page.waitForTimeout(700);await page.mouse.move(720,899);actions.push({elapsedMs:Date.now()-start,pointer:{x:720,y:899},name:'exit-to-hero-bottom'});await page.waitForTimeout(700);
 await cdp.send('Page.stopScreencast');await Promise.all(writes);await fs.writeFile(folder+'/timeline.json',JSON.stringify({url,browser:browser.version(),frames,actions,note:'CDP continuous screencast; browser frame timestamps retained. Original clock is not controlled; playback is diagnostic, not an exact motion score.'},null,2));await context.close();console.log(label,frames.length);
}}finally{await browser.close();}

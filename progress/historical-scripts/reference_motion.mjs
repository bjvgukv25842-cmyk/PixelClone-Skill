import {chromium} from 'playwright';
import fs from 'node:fs/promises';
const root='../outputs/pixelclone-review';
const browser=await chromium.launch({channel:'msedge',headless:true});
try {
 const page=await browser.newPage({viewport:{width:1440,height:900}});await page.goto('https://monopo.london/',{waitUntil:'domcontentloaded'});await page.waitForTimeout(10000);
 await fs.mkdir(root+'/reference/motion',{recursive:true});const times=[],start=Date.now();
 for(let i=0;i<30;i++){const t=i/29,x=720+400*Math.sin(t*Math.PI*2),y=450-170*Math.sin(t*Math.PI*4);await page.mouse.move(x,y);await page.waitForTimeout(65);await page.screenshot({path:root+'/reference/motion/frame-'+String(i).padStart(3,'0')+'.png'});times.push({i,elapsedMs:Date.now()-start,pointer:{x,y}});}
 await fs.writeFile(root+'/reference/motion/timeline.json',JSON.stringify({note:'Sampled continuous pointer replay; wall-clock timestamps retained. Encoded preview is constant-rate and not a scoring clock.',frames:times},null,2));
 await page.setViewportSize({width:390,height:844});await page.reload({waitUntil:'domcontentloaded'});await page.waitForTimeout(6000);await page.screenshot({path:root+'/reference/mobile-inspection.png'});
}finally{await browser.close();}

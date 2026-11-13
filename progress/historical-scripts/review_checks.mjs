import {chromium} from 'playwright';
import fs from 'node:fs/promises';
import {capturePage} from '../toolkit/browser.mjs';
import {compareFiles} from '../toolkit/compare.mjs';
import {writeReport} from '../toolkit/report.mjs';
const root='../outputs/pixelclone-review';
for(const arm of ['control','old','candidate']){
 const url=`http://127.0.0.1:8765/${arm}/index.html`;
 const c=await capturePage({url,channel:'msedge',viewport:{width:1440,height:900},actions:[{type:'wait',ms:700}],regions:[{name:'heading',selector:'h1'}]},`${root}/${arm}/desktop-capture`);
 const m=await capturePage({url,channel:'msedge',viewport:{width:390,height:844},regions:[{name:'heading',selector:'h1'}]},`${root}/${arm}/mobile-capture`);
 const cmp=await compareFiles('work/reference/desktop.png',`${root}/${arm}/desktop-capture/screenshot.png`,`${root}/${arm}/comparison`,{regions:[{name:'hero',x:300,y:280,width:820,height:320},{name:'navigation',x:40,y:20,width:1150,height:110}]});await writeReport(`${root}/${arm}/comparison`);
 console.log(arm,JSON.stringify({diff:cmp.page.ratio,regions:cmp.regions,overflowDesktop:c.overflow,overflowMobile:m.overflow,errors:c.errors}));
}
const browser=await chromium.launch({channel:'msedge',headless:true});
try{
 for(const arm of ['control','old','candidate']){
  const context=await browser.newContext({viewport:{width:1440,height:900}});const page=await context.newPage();await page.goto(`http://127.0.0.1:8765/${arm}/index.html`);await page.evaluate(()=>document.fonts.ready);
  const errors=[];page.on('pageerror',e=>errors.push(e.message));const states=[];await fs.mkdir(`${root}/${arm}/motion`,{recursive:true});
  for(const [i,point] of [[720,450],[300,300],[720,250],[1100,500],[720,450]].entries()){
   await page.mouse.move(...point);await page.waitForTimeout(350);await page.screenshot({path:`${root}/${arm}/motion/frame-${String(i).padStart(3,'0')}.png`});states.push({index:i,pointer:{x:point[0],y:point[1]},settleMs:350});
  }
  const accept=page.getByRole('button',{name:'ACCEPT',exact:true});let cookies=false;
  if(await accept.count()){await accept.click();cookies=!(await accept.isVisible());}
  await page.setViewportSize({width:390,height:844});let menu=false,escape=false;
  const toggle=page.locator('button[aria-expanded]').first();if(await toggle.count()){await toggle.first().click();menu=(await toggle.first().getAttribute('aria-expanded'))==='true';await page.keyboard.press('Escape');escape=(await toggle.first().getAttribute('aria-expanded'))==='false';}
  await fs.writeFile(`${root}/${arm}/developer-qa.json`,JSON.stringify({browser:browser.version(),errors,cookieDismissed:cookies,mobileMenuExpanded:menu,escapeCloses:escape,states,scope:'mechanical behavior only; does not prove original motion similarity'},null,2));await context.close();
 }
}finally{await browser.close();}


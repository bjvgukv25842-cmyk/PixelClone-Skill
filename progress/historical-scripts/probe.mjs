import {chromium} from 'playwright';
import fs from 'node:fs/promises';
const out='work/reference'; await fs.mkdir(out,{recursive:true});
const browser=await chromium.launch({headless:true,channel:"msedge"});
const page=await browser.newPage({viewport:{width:1440,height:900},deviceScaleFactor:1});
const resources=[];page.on('response',r=>{const type=r.request().resourceType();if(['image','font','media'].includes(type))resources.push({url:r.url(),type,status:r.status()});});
try {await page.goto('https://monopo.london',{waitUntil:'domcontentloaded',timeout:60000}); await page.waitForTimeout(10000);await page.screenshot({path:out+'/desktop.png'});await fs.writeFile(out+'/resources.json',JSON.stringify(resources,null,2));await fs.writeFile(out+'/dom.json',JSON.stringify(await page.evaluate(()=>({text:document.body.innerText,fonts:[...document.fonts].map(f=>({family:f.family,status:f.status})),elements:[...document.querySelectorAll('h1,header,canvas,nav')].map(e=>({tag:e.tagName,cls:e.className,rect:e.getBoundingClientRect().toJSON()})),styles:[...document.querySelectorAll('link[rel=stylesheet]')].map(e=>e.href)})),null,2));console.log(JSON.stringify({title:await page.title(),resources:resources.length}));}finally{await browser.close();}


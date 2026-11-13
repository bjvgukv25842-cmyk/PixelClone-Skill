import {chromium} from 'playwright';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import os from 'node:os';
import {installRenderAudit} from './render-audit.mjs';

export async function capturePage(config,out){
 if(!/^https?:\/\//.test(config.url??''))throw Error('url must be HTTP(S)');
 const viewport=config.viewport??{width:1440,height:900},timeout=config.timeoutMs??30000;
 if(!Number.isFinite(timeout)||timeout<=0)throw Error('timeoutMs must be finite and positive');
 if(![viewport.width,viewport.height].every(x=>Number.isInteger(x)&&x>0))throw Error('Invalid viewport');
 const dpr=config.deviceScaleFactor??1;if(!Number.isFinite(dpr)||dpr<=0)throw Error('Invalid DPR');
 const channel=config.channel??process.env.PIXELCLONE_BROWSER_CHANNEL;
 const browser=await chromium.launch({headless:true,...(channel?{channel}:{})});
 let context;
 try{
 await fs.mkdir(out,{recursive:true});
 context=await browser.newContext({viewport,deviceScaleFactor:dpr,...(config.hasTouch!==undefined?{hasTouch:config.hasTouch}:{}),...(config.isMobile!==undefined?{isMobile:config.isMobile}:{}),locale:config.locale??'en-GB',timezoneId:config.timezoneId??'UTC',colorScheme:config.colorScheme??'light',reducedMotion:config.reducedMotion??'no-preference',...(config.recordVideo?{recordVideo:{dir:path.join(out,'video'),size:viewport}}:{})});
 const page=await context.newPage();
 if(config.renderAudit)await page.addInitScript(installRenderAudit);
 page.setDefaultTimeout(timeout);
 const resources=[],errors=[],failedRequests=[],consoleErrors=[];
 page.on('pageerror',e=>errors.push(e.message));
 page.on('console',m=>{if(m.type()==='error'&&consoleErrors.length<100)consoleErrors.push({text:m.text().slice(0,4000),location:m.location()});});
 page.on('requestfailed',r=>failedRequests.push({url:r.url(),error:r.failure()?.errorText}));
 page.on('response',r=>{if(['image','font','media','stylesheet'].includes(r.request().resourceType()))resources.push({url:r.url(),type:r.request().resourceType(),status:r.status(),contentType:r.headers()['content-type']??null});});
  await page.goto(config.url,{waitUntil:'domcontentloaded',timeout});
  if(config.readySelector)await page.locator(config.readySelector).waitFor({state:'visible'});
  for(const action of config.actions??[]){
   switch(action.type){
    case 'click':await page.locator(action.selector).click();break;
    case 'hover':await page.locator(action.selector).hover();break;
    case 'scroll':await page.evaluate(({x=0,y})=>window.scrollTo(x,y),action);break;
    case 'pointer':await page.mouse.move(action.x,action.y);break;
    case 'wait':if(!Number.isFinite(action.ms)||action.ms<0||action.ms>30000)throw Error('Invalid wait');await page.waitForTimeout(action.ms);break;
    case 'press':await page.keyboard.press(action.key);break;
    case 'drag':await page.locator(action.from).dragTo(page.locator(action.to));break;
    default:throw Error(`Unsupported action ${action.type}`);
   }
  }
  if(config.state){
   await page.waitForFunction(()=>typeof window.__pixelclone?.setState==='function',null,{timeout});
   await page.evaluate(async ({state,timeout})=>{
    let timer;try{await Promise.race([(async()=>{await window.__pixelclone.ready;await window.__pixelclone.setState(state);await window.__pixelclone.render?.();})(),new Promise((_,reject)=>{timer=setTimeout(()=>reject(Error('Motion adapter timed out')),timeout);})]);}finally{clearTimeout(timer);}
   },{state:config.state,timeout});
  }
  const backgroundLoads=await page.evaluate(async ms=>{
   const urls=new Set();for(const element of document.querySelectorAll('*')){
    const rect=element.getBoundingClientRect();if(rect.bottom<0||rect.top>innerHeight||rect.right<0||rect.left>innerWidth)continue;
    for(const pseudo of [null,'::before','::after'])for(const match of getComputedStyle(element,pseudo).backgroundImage.matchAll(/url\((?:"([^"]*)"|'([^']*)'|([^)]*))\)/g))urls.add(match[1]??match[2]??match[3]);
   }
   const backgrounds=Promise.all([...urls].map(async url=>{const image=new Image();image.src=url;try{await image.decode();return {url,loaded:true};}catch{return {url,loaded:false};}}));
   let timer;let results;try{results=await Promise.race([Promise.all([backgrounds,document.fonts.ready,...[...document.images].filter(i=>i.loading!=='lazy'||i.getBoundingClientRect().top<innerHeight).map(i=>i.decode().catch(()=>null))]),new Promise((_,reject)=>{timer=setTimeout(()=>reject(Error('Resources did not settle')),ms);})]);}finally{clearTimeout(timer);}
   await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   return results[0];
  },timeout);
  if(config.animationMode==='static')await page.evaluate(async()=>{
   for(const animation of document.getAnimations()){
    const timing=animation.effect?.getComputedTiming();
    if(timing&&Number.isFinite(timing.endTime)){try{animation.finish();}catch{animation.pause();}}
    else{animation.pause();animation.currentTime=0;}
   }
   await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
  });
  const data=await page.evaluate(regions=>{
   const rect=e=>{const b=e.getBoundingClientRect();return {x:b.x,y:b.y,width:b.width,height:b.height};};
   return {title:document.title,scroll:{x:scrollX,y:scrollY},overflow:document.documentElement.scrollWidth>innerWidth,
    fonts:[...document.fonts].map(f=>({family:f.family,weight:f.weight,style:f.style,status:f.status})),
    images:[...document.images].map(i=>({src:i.currentSrc||i.src,loaded:i.complete&&i.naturalWidth>0,naturalWidth:i.naturalWidth,naturalHeight:i.naturalHeight,rect:rect(i)})),
    backgrounds:[...document.querySelectorAll('*')].filter(e=>getComputedStyle(e).backgroundImage!=='none').map(e=>({tag:e.tagName,background:getComputedStyle(e).backgroundImage,rect:rect(e)})),
    svg:[...document.querySelectorAll('svg')].map(e=>({rect:rect(e),markup:e.outerHTML})),
    media:[...document.querySelectorAll('video,canvas')].map(e=>({tag:e.tagName,src:e.currentSrc??null,rect:rect(e)})),
    regions:regions.map(r=>{const e=document.querySelector(r.selector);if(!e)return {...r,missing:true};const c=getComputedStyle(e);const range=document.createRange();range.selectNodeContents(e);const lines=new Set([...range.getClientRects()].filter(b=>b.width&&b.height).map(b=>Math.round(b.y)));return {...r,rect:rect(e),text:e.textContent,lines:lines.size,style:Object.fromEntries(['fontFamily','fontSize','fontWeight','fontStyle','fontStretch','fontVariationSettings','fontFeatureSettings','fontKerning','fontVariantLigatures','textRendering','webkitFontSmoothing','letterSpacing','lineHeight','color','backgroundColor','transform'].map(k=>[k,c[k]]))};})};
  },config.regions??[]);
  const cdp=await context.newCDPSession(page);await cdp.send('DOM.enable');await cdp.send('CSS.enable');const {root}=await cdp.send('DOM.getDocument');
  for(const region of data.regions){if(region.missing)continue;try{const {nodeId}=await cdp.send('DOM.querySelector',{nodeId:root.nodeId,selector:region.selector});region.actualFonts=(await cdp.send('CSS.getPlatformFontsForNode',{nodeId})).fonts;}catch(e){region.fontAuditError=e.message;}}
  const renderAudit=config.renderAudit?await page.evaluate(()=>window.__pixelcloneRenderAudit?.()??null):null;
  if(renderAudit)for(const shader of renderAudit.shaders)shader.sha256=crypto.createHash('sha256').update(shader.source).digest('hex');
  const file=path.join(out,'screenshot.png');await page.screenshot({path:file,fullPage:config.fullPage??false,animations:'allow',caret:'hide'});
  const result={schemaVersion:1,capturedAt:new Date().toISOString(),browserVersion:browser.version(),channel:channel??'bundled-chromium',platform:os.platform(),release:os.release(),config,viewport,deviceScaleFactor:dpr,...data,backgroundLoads,resources,failedRequests,errors,screenshotSha256:crypto.createHash('sha256').update(await fs.readFile(file)).digest('hex'),stateControlled:!!config.state};
  result.consoleErrors=consoleErrors;
  if(config.renderAudit)result.renderAudit=renderAudit;
  await fs.writeFile(path.join(out,'capture.json'),JSON.stringify(result,null,2));return result;
 }finally{
  let timer;
  try{if(context)await Promise.race([context.close(),new Promise((_,reject)=>{timer=setTimeout(()=>reject(Error('Browser context/video finalization timed out')),10000);})]);}
  finally{clearTimeout(timer);await browser.close();}
 }
}

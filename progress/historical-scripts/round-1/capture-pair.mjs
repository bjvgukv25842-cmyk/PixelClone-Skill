import {chromium} from 'playwright';import fs from 'node:fs/promises';import {compareFiles} from '../../toolkit/compare.mjs';import {writeReport} from '../../toolkit/report.mjs';
const out='../outputs/pixelclone-review/round-1';await fs.cp('cases/monopo-r1',out+'/candidate',{recursive:true});
const browser=await chromium.launch({channel:'msedge',headless:true});const comparison=[];
const points=[{name:'initial',pointer:null},{name:'left',pointer:{x:440,y:400}},{name:'quarter',pointer:{x:600,y:440}},{name:'center',pointer:{x:720,y:450}},{name:'three-quarter',pointer:{x:850,y:470}},{name:'right',pointer:{x:1040,y:500}},{name:'reverse',pointer:{x:720,y:450}},{name:'exit',pointer:{x:720,y:890}}];
try{
 for(const [label,url] of [['reference','https://monopo.london/'],['candidate','http://127.0.0.1:8765/round-1/candidate/index.html']]){
  await fs.mkdir(out+'/'+label+'/frames',{recursive:true});const context=await browser.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1});const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto(url,{waitUntil:'domcontentloaded',timeout:60000});await page.waitForTimeout(9000);const timeline=[];
  for(const point of points){if(point.pointer)await page.mouse.move(point.pointer.x,point.pointer.y);const start=Date.now();await page.waitForTimeout(1500);await page.screenshot({path:out+'/'+label+'/frames/'+point.name+'.png'});timeline.push({...point,settleMs:1500,actualElapsedMs:Date.now()-start});}
  await fs.writeFile(out+'/'+label+'/timeline.json',JSON.stringify({browser:browser.version(),viewport:{width:1440,height:900},states:timeline,errors,note:'Real pointer replay with settle time. Neither reference clock nor frame cadence is controlled. Scores are diagnostic.'},null,2));
  await context.close();
 }
 for(const point of points){const result=await compareFiles(out+'/reference/frames/'+point.name+'.png',out+'/candidate/frames/'+point.name+'.png',out+'/comparisons/'+point.name,{regions:[{name:'heading',x:300,y:300,width:820,height:290},{name:'lens-center',x:595,y:325,width:250,height:250}]});await writeReport(out+'/comparisons/'+point.name);comparison.push({state:point.name,page:result.page,regions:result.regions,withinTolerance:result.withinTolerance});}
 await fs.writeFile(out+'/comparison-summary.json',JSON.stringify(comparison,null,2));console.log(comparison.map(x=>({state:x.state,page:x.page.ratio,regions:x.regions.map(r=>({name:r.name,ratio:r.ratio}))})));
}finally{await browser.close();}

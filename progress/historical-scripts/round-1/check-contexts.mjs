import {capturePage} from '../../toolkit/browser.mjs';import {compareFiles} from '../../toolkit/compare.mjs';import {writeReport} from '../../toolkit/report.mjs';import fs from 'node:fs/promises';
const out='../outputs/pixelclone-review/round-1';
for(const [label,url] of [['reference','https://monopo.london/'],['candidate','http://127.0.0.1:8765/round-1/candidate/index.html']]){
 for(const [mode,extra] of [['mobile',{viewport:{width:390,height:844},hasTouch:true,isMobile:true}],['reduced',{viewport:{width:1440,height:900},reducedMotion:'reduce'}]]){
  const r=await capturePage({url,channel:'msedge',...extra,actions:[{type:'wait',ms:8000}],regions:[{name:'heading',selector:'h1'}]},out+'/'+label+'/'+mode);console.log(label,mode,{overflow:r.overflow,errors:r.errors,consoleErrors:r.consoleErrors,heading:r.regions[0].rect});
 }
}
for(const mode of ['mobile','reduced']){await compareFiles(out+'/reference/'+mode+'/screenshot.png',out+'/candidate/'+mode+'/screenshot.png',out+'/comparisons/'+mode,{});await writeReport(out+'/comparisons/'+mode);}
// The updated diagnostic should expose the reference raster-text/render graph.
await capturePage({url:'https://monopo.london/',channel:'msedge',renderAudit:true,actions:[{type:'wait',ms:8000}]},'work/round-1/render-audit');

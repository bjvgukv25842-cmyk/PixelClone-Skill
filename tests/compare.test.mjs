import test from 'node:test';
import assert from 'node:assert/strict';
import { PNG } from 'pngjs';
import { compareImages } from '../toolkit/compare.mjs';
import { compareLayout } from '../toolkit/compare.mjs';
import { summarizeRuns } from '../toolkit/report.mjs';

function solid(w=100,h=100) { const p=new PNG({width:w,height:h}); p.data.fill(255); return p; }
test('identical images are exactly equal',()=>{
 const r=compareImages(solid(),solid()); assert.equal(r.exact,true); assert.equal(r.withinTolerance,true);
});
test('small critical region fails even when the page passes',()=>{
 const a=solid(), b=solid(); b.data.fill(0,0,4);
 const r=compareImages(a,b,{regions:[{name:'logo',x:0,y:0,width:2,height:2}]});
 assert.equal(r.page.pass,true); assert.equal(r.regions[0].pass,false); assert.equal(r.withinTolerance,false); assert.equal(r.exact,false);
});
test('dimensions and invalid bounds cannot be silently normalized',()=>{
 assert.throws(()=>compareImages(solid(),solid(99,100)),/dimensions/);
 assert.throws(()=>compareImages(solid(),solid(),{threshold:NaN}),/threshold/);
 assert.throws(()=>compareImages(solid(),solid(),{regions:[{name:'bad',x:-1,y:0,width:2,height:2}]}),/region/);
});
test('tolerance does not imply exact equality',()=>{
 const a=solid(),b=solid(); b.data[0]=254; const r=compareImages(a,b);
 assert.equal(r.exact,false); assert.equal(r.withinTolerance,true);
});
test('failed, pending, and timed-out runs remain visible in denominator',()=>{
 const r=summarizeRuns([{status:'passed'},{status:'failed'},{status:'timeout'},{status:'pending'},{status:'infrastructure_error'}]);
 assert.equal(r.total,5); assert.equal(r.passed,1); assert.equal(r.successRate,0.2); assert.equal(r.infrastructureErrors,1);
});
test('layout flags changed line count and missing or shifted regions',()=>{
 const a={viewport:{width:800,height:600},regions:[{name:'title',lines:1,rect:{x:0,y:0,width:500,height:40}}]};
 const b={...a,regions:[{name:'title',lines:2,rect:{x:3,y:0,width:500,height:40}}]};
 assert.equal(compareLayout(a,b).pass,false);
 assert.equal(compareLayout(a,{...a,regions:[]}).pass,false);
 assert.equal(compareLayout(a,a).pass,true);
});
test('run summary rejects duplicate case IDs rather than counting retries as cases',()=>{
 assert.throws(()=>summarizeRuns([{caseId:'a',status:'failed'},{caseId:'a',status:'passed'}]),/duplicate/i);
});
test('collapsed actual region is not accepted by anchor tolerance',()=>{
 const a={viewport:{width:100,height:100},regions:[{name:'divider',lines:0,rect:{x:0,y:0,width:100,height:1}}]};
 assert.equal(compareLayout(a,{...a,regions:[{...a.regions[0],rect:{...a.regions[0].rect,height:0}}]}).pass,false);
});

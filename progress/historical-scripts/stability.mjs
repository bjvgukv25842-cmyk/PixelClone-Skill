import fs from 'node:fs/promises';
import {compareFiles} from '../toolkit/compare.mjs';
const results=[];
for(const [a,b] of [[1,2],[1,3],[2,3]]){const r=await compareFiles(`work/reference/run-${a}/screenshot.png`,`work/reference/run-${b}/screenshot.png`,`work/reference/stability-${a}-${b}`);results.push({pair:[a,b],ratio:r.page.ratio,exact:r.exact,withinTolerance:r.withinTolerance});}
await fs.writeFile('work/reference/stability.json',JSON.stringify({schemaVersion:1,stable:results.every(r=>r.withinTolerance),comparisons:results,note:'Live reference animation is not frame-controlled; comparisons are diagnostic.'},null,2));console.log(results);

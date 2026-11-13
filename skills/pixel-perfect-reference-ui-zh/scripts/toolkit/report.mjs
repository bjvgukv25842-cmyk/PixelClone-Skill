import fs from 'node:fs/promises';
import path from 'node:path';
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function summarizeRuns(runs){
 const statuses=['passed','failed','timeout','pending','infrastructure_error'];
 if(!Array.isArray(runs)||runs.some(r=>!statuses.includes(r.status)))throw Error('Invalid run status');
 const ids=runs.map(r=>r.caseId).filter(Boolean);if(new Set(ids).size!==ids.length)throw Error('Duplicate case IDs: keep retries under the same case record');
 const total=runs.length,passed=runs.filter(r=>r.status==='passed').length;
 return {total,passed,successRate:total?passed/total:null,pending:runs.filter(r=>r.status==='pending').length,infrastructureErrors:runs.filter(r=>r.status==='infrastructure_error').length};
}
export async function writeReport(dir){
 const read=async name=>{try{return JSON.parse(await fs.readFile(path.join(dir,name),'utf8'));}catch(e){if(e.code==='ENOENT')return null;throw e;}};
 const comparison=await read('comparison.json'),evaluation=await read('evaluation.json'),capture=await read('capture.json');
 if(!comparison&&!evaluation&&!capture)throw Error('No comparison.json, evaluation.json or capture.json found');
 const summary=evaluation?.runs?summarizeRuns(evaluation.runs):null;
 const checks=evaluation?.requirements??[];
 const completion=checks.length?checks.filter(c=>c.status==='passed').length/checks.length:null;
 const title=comparison?(comparison.exact?'逐像素一致（仅本截图）':comparison.withinTolerance?'截图达到配置容差':'截图未达到配置容差'):'待评价';
 const html=`<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>PixelClone 评审</title><style>body{font:16px/1.65 system-ui;max-width:1300px;margin:40px auto;padding:0 24px;background:#f4f5f7;color:#18212b}h1{font-size:28px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}img{width:100%;background:white}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:white;padding:20px;border-radius:12px}small{color:#465367}</style><h1>${escape(title)}</h1><p>图像容差、需求完成率、人工评分分别报告。截图结果不代表功能或动态已通过。</p>${comparison?'<div class="grid">'+['reference','actual','overlay','diff'].map(n=>`<figure><figcaption>${n}</figcaption><img src="${n}.png"></figure>`).join('')+'</div>':''}<h2>结果与证据</h2><pre>${escape(JSON.stringify({completion,summary,comparison,capture,evaluation},null,2))}</pre><p>人工反馈保存在 evaluation.json 的 humanReview 字段；未收到评价时保持 null。</p></html>`;
 await fs.writeFile(path.join(dir,'report.html'),html);return {completion,summary,report:path.resolve(dir,'report.html')};
}

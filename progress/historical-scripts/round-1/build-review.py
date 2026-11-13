from pathlib import Path
import json,hashlib,shutil,zipfile,html

repo=Path('.');outputs=Path('../outputs');root=outputs/'pixelclone-review';out=root/'round-1'
def read(p): return json.loads(Path(p).read_text(encoding='utf8'))
def write(p,x): Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf8')
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
comparison=read(out/'comparison-summary.json');feedback=read(out/'feedback-r0.json');qa=read('work/round-1/qa/checks.json')
mobile=read(out/'comparisons/mobile/comparison.json');reduced=read(out/'comparisons/reduced/comparison.json');stability=read(out/'reference/stability/stability.json')
evaluation={
 'schemaVersion':1,'caseId':'monopo-development','round':'r1','skillVersion':'0.3.0','reviewDate':'2026-11-06',
 'runType':'maintainer source-assisted development repair; not a clean benchmark trial',
 'inputTrack':'website-resources','sourceAccess':'runtime-and-published-source','priorFeedback':feedback['humanReview'],'humanReview':None,
 'status':'awaiting-human-review; full fidelity acceptance not passed','completionRate':None,'taskSuccessRate':None,
 'reasonForNoAggregateRate':'This is one development repair with changed inputs, not a frozen multi-case success-rate experiment. Human completion remains a separate score.',
 'desktopSamples':comparison,'mobile':mobile,'reducedMotion':reduced,'referenceStability':stability,'mechanicalChecks':qa,
 'motion':{'status':'human-review-pending','capture':'CDP screencast + source browser timestamps, VFR MP4','timeSynchronized':False},
 'limitations':['Published rendering source/runtime evidence was added; no causal comparison with r0 is claimed.','Entry easing is not frame-calibrated.','Lens overlaps bottom content in the boundary sample; failed ROI is retained.','Touch menu differs from the reference initial viewport.','Downstream destination sections remain scoped placeholders.','Continuous motion and overall acceptance require human review.','12 holdout cases remain unrun and uninspected for tuning.'],
 'validation':{'nodeTests':19,'pythonTests':6,'caseChecks':len(qa['checks']),'skillForwardTest':'independent evidence-contract application, not a full reconstruction trial','remoteCI':'not run'},
}
write(out/'evaluation.json',evaluation)
contract={'schemaVersion':1,'inputTrack':'website-resources','sourceAccess':'runtime-and-published-source','scope':'navigation, hero, pointer lens, cookies, desktop and touch viewport','reference':'https://monopo.london/','viewports':[{'width':1440,'height':900,'dpr':1,'hasTouch':False},{'width':390,'height':844,'dpr':1,'hasTouch':True}],
 'layers':[{'role':'background','renderer':'WebGL2 derivative-noise gradient copied from submitted reference shader with license comment preserved','sourceManifest':'sources.json'},{'role':'lens','renderer':'Pixi Sprite from original lense.png'},{'role':'English title','renderer':'Pixi Text + inverse circular mask','font':'Roobert-Regular.woff2','semanticDOM':'h1'},{'role':'Japanese title','renderer':'Pixi Text -> displacement filter -> circular mask','font':'NotoSansCJKjp-Regular.woff2'},{'role':'color fringe','renderer':'duplicate Japanese Text -> displacement -> RGB split -> original sprite mask'}],
 'typography':{'evidence':'reference runtime.json plus original resource hashes and screenshot ROIs','rasterization':'reference padding/trim and measured font sizes, Pixi 6.2.0','DPR':'capped at 2 for local GPU; scored viewport DPR=1','touch':'real DOM at measured bounds','OpenType':'liga/kern and optimizeLegibility inspected separately from font identity'},
 'response':{'coordinates':'CSS px relative to hero','forceTarget':'pointer.x / width * 5','seedTarget':'pointer.y / height * 2 - 1','smoothing':'0.1 each RAF, matching observed reference update','lensRadius':125,'displacementScale':[20,20],'colorSplit':{'red':[-2,2],'green':[1,1],'blue':[2,-2]},'pointerLeave':'retain last valid position','touch':'no desktop lens; fixed original mobile gradient','reducedMotion':'fixed representative scene; usable DOM controls'},
 'checks':qa['checks'],'visualEvidence':'workspace outputs/pixelclone-review/round-1/comparison-summary.json','unknown':['entry timing equivalence','all intermediate motion frame equivalence','all downstream routes']}
write('cases/monopo-r1/render-contract.json',contract)
shutil.copy2('cases/monopo-r1/scene.mjs',out/'candidate/scene.mjs')
shutil.copy2('cases/monopo-r1/render-contract.json',out/'candidate/render-contract.json')
shutil.copy2('cases/monopo-r1/verify.mjs',out/'candidate/verify.mjs')
shutil.copy2('cases/monopo-r1/README.md',out/'candidate/README.md')
shutil.copy2('work/round-1/qa/checks.json',out/'candidate/checks.json')
shutil.copy2('work/round-1/independent-skill-check/render-contract.json',out/'independent-skill-check.json')
freeze={'version':'0.3.0','finalCandidateFrozenDate':'2026-11-06','roundType':'development repair; not a frozen-from-scratch scored trial','model':'inherited model; exact model identity/budget not recorded','inputsExpanded':True,'files':{}}
for folder in ['toolkit','skills','cases/monopo-r1']:
 for p in Path(folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts: freeze['files'][p.as_posix()]=digest(p)
freeze['referenceFrames']={p.name:digest(p) for p in (out/'reference/frames').glob('*.png')}
freeze['referenceShaderEvidenceSha256']=digest('work/round-1/source/probe.json');freeze['priorFeedbackSha256']=digest(out/'feedback-r0.json')
write(out/'freeze.json',freeze)

style='''*{box-sizing:border-box}body{margin:0;color:#17212e;background:#eef1f5;font:16px/1.7 system-ui}main{max-width:1440px;margin:auto;padding:32px 24px}h1{font-size:32px;line-height:1.3}h2{font-size:22px}p{max-width:1100px}section{background:#fff;border:1px solid #d8e0e9;padding:24px;border-radius:14px;margin:22px 0}.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}img,video{width:100%;display:block;background:#111;border-radius:6px}a{color:#155278}button,select,input,textarea{font:inherit;border:1px solid #a7b8c5;border-radius:8px;padding:10px;background:white}button,.primary{background:#173e57;color:white;border-radius:8px;padding:10px 16px;border:0;cursor:pointer;display:inline-block;text-decoration:none}.tools{display:flex;align-items:center;gap:16px;flex-wrap:wrap}.badge{background:#fff0dd;color:#8b431b;display:inline-block;padding:5px 14px;border-radius:20px}.overlay{position:relative}.overlay img:last-child{position:absolute;inset:0}.rating{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.rating input{width:100%}label{display:block;margin:12px 0}textarea{width:100%;min-height:130px}table{border-collapse:collapse;width:100%}td,th{padding:9px;text-align:left;border-bottom:1px solid #dce3e9}.pass{color:#177355}.fail{color:#a13726}small{color:#586b7b}.notice{border-left:4px solid #b96029;padding-left:14px}@media(max-width:800px){.grid,.rating{grid-template-columns:1fr}main{padding:22px 12px}section{padding:16px}h1{font-size:25px}}'''
page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,"><title>PixelClone · 字体与动效第二轮评审</title><style>STYLE</style><main>
<p>PIXELCLONE / DEVELOPMENT REPAIR R1 / v0.3</p><h1>字体与鼠标形变 · 第二轮评审</h1><p class="badge">上一轮：70／60／40 · 不接受 ｜ 本轮待你评价</p>
<p>已把圆形覆盖层替换为真正作用于文字像素的位移、遮罩与色散，背景随鼠标改变。移动端使用独立的触屏表现。你的原始反馈、上一轮页面和失败证据全部保留。</p>
<div class="tools"><a class="primary" href="candidate/index.html" target="_blank" rel="noopener">打开新版，移动鼠标体验 ↗</a><a href="../candidate/index.html" target="_blank">打开上一轮复刻 ↗</a><a href="https://monopo.london/" target="_blank" rel="noopener">原站 ↗</a><a href="../round-0.html">上一轮三组对照</a></div>
<p class="notice">本轮增加了原站源码与运行时诊断，是开发修复，不是等条件 benchmark。不会将像素差异换算成“人眼相似度”，也不据此宣称通用成功率提升。</p>
<section><h2>同一状态的画面对照</h2><div class="tools"><label>采样状态 <select id="state"></select></label><a id="report" target="_blank">查看差异报告 ↗</a></div><p id="metric"></p><div class="grid"><div><strong>参考页面 · 1440 × 900</strong><img id="reference" alt="原站状态截图"></div><div><strong>本轮复刻</strong><img id="candidate" alt="本轮状态截图"></div></div><p><small>参考时钟没有冻结，导航时间会产生差异。标题、随指针移动的透镜、导航和底部文案均计入检查。</small></p></section>
<section><h2>叠加检查</h2><label>新版图透明度 <input id="opacity" type="range" min="0" max="1" value="0.5" step="0.01"></label><div class="overlay"><img id="under" alt="参考底图"><img id="over" style="opacity:.5" alt="复刻叠加图"></div></section>
<section><h2>连续动作</h2><p>重点观察鼠标扫过字形时的折射、色边和跟随滞后，以及停顿与反向过程。录像保留浏览器帧间隔，但原站时钟未受控，不能作为严格逐帧同步成绩。</p><button id="play">一起从头播放</button><div class="grid"><div><strong>参考</strong><video id="refVideo" src="reference/preview.mp4" controls muted playsinline></video></div><div><strong>本轮</strong><video id="newVideo" src="candidate/preview.mp4" controls muted playsinline></video></div></div></section>
<section><h2>触屏移动端与检查结果</h2><p id="mobileMetric"></p><div class="grid"><img src="reference/mobile/screenshot.png" style="max-width:390px;margin:auto" alt="触屏参考"><img src="candidate/mobile/screenshot.png" style="max-width:390px;margin:auto" alt="触屏复刻"></div><table><thead><tr><th>状态</th><th>全页差异</th><th>标题</th><th>透镜</th><th>全部所选区域</th></tr></thead><tbody id="rows"></tbody></table><p><a href="candidate/checks.json">9 项案例行为检查</a> · <a href="reference/stability/stability.json">参考稳定性</a> · <a href="comparisons/mobile/report.html">移动端差异</a> · <a href="comparisons/reduced/report.html">减少动态效果</a></p></section>
<section><h2>本轮仍需验收的部分</h2><p>底部边界状态、移动端细部仍保留失败区域。入场节奏未逐帧校准；下游内容仍为范围外的演示段落。9 项行为检查通过，不等于整页或完整动效通过。12 个独立验证案例尚未运行。</p></section>
<section><h2>你的第二轮反馈</h2><p>上一轮反馈已记录：视觉 70、完成度 60、动效 40，不接受。请评价这次的新页面；输入会暂存在此浏览器，也可以直接在聊天中反馈。</p><form id="feedback"><div class="rating"><label>视觉相似度（0–100）<input name="visual" type="number" min="0" max="100"></label><label>完成度（0–100）<input name="completion" type="number" min="0" max="100"></label><label>动效还原（0–100）<input name="motion" type="number" min="0" max="100"></label></div><label>是否接受本轮 <select name="accepted"><option value="pending">尚未决定</option><option value="yes">接受</option><option value="no">不接受</option></select></label><label>最明显的剩余差异<textarea name="comments" placeholder="例如：字体失真已接近；鼠标快速反向时仍有差异……"></textarea></label><button type="submit">导出第二轮反馈</button> <span id="saved" role="status"></span></form></section>
<section><h2>本轮文件</h2><p><a href="../../pixelclone-skills-v0.3-candidate.zip">中英文 skill 安装包</a> · <a href="../../PixelClone-Skill-v0.3-source.zip">工具与案例源码</a> · <a href="evaluation.json">完整评测记录</a> · <a href="freeze.json">版本和输入哈希</a> · <a href="feedback-r0.json">你的上一轮反馈</a> · <a href="candidate/render-contract.json">渲染证据合同</a></p><p><small>工具 19 项 Node 与 6 项 Python 测试通过；候选包共用同一套工具。安装包不包含原站商业素材。源码包中的案例代码依赖本地评审目录的原始资源。</small></p></section></main><script>
const data=DATA, labels={initial:'初始',left:'左侧',quarter:'经过标题',center:'中心', 'three-quarter':'向右',right:'右侧',reverse:'反向回到中心',exit:'移至底部边界'};
const selector=document.querySelector('#state'),percent=x=>(x*100).toFixed(3)+'%';
for(const r of data.desktopSamples){const o=document.createElement('option');o.value=r.state;o.textContent=labels[r.state];selector.append(o);const tr=document.createElement('tr');const values=[labels[r.state],percent(r.page.ratio),percent(r.regions[0].ratio),percent(r.regions[1].ratio),r.withinTolerance?'达到容差':'未达到容差'];for(const [i,value]of values.entries()){const td=document.createElement('td');td.textContent=value;if(i===4)td.className=r.withinTolerance?'pass':'fail';tr.append(td)}document.querySelector('#rows').append(tr)}
function update(){const name=selector.value,r=data.desktopSamples.find(x=>x.state===name);document.querySelector('#reference').src=document.querySelector('#under').src='reference/frames/'+name+'.png';document.querySelector('#candidate').src=document.querySelector('#over').src='candidate/frames/'+name+'.png';document.querySelector('#report').href='comparisons/'+name+'/report.html';document.querySelector('#metric').textContent='全页差异 '+percent(r.page.ratio)+' ｜ 标题区域 '+percent(r.regions[0].ratio)+' ｜ 透镜区域 '+percent(r.regions[1].ratio)+' ｜ 全部所选区域：'+(r.withinTolerance?'达到配置容差':'仍有区域未达容差')+'。不是人眼相似度百分比。';}
selector.onchange=update;update();document.querySelector('#opacity').oninput=e=>document.querySelector('#over').style.opacity=e.target.value;document.querySelector('#mobileMetric').textContent='390 × 844，触屏上下文。全页差异 '+percent(data.mobile.page.ratio)+'；关键区域：'+(data.mobile.withinTolerance?'达到配置容差':'仍未达到配置容差')+'。';
document.querySelector('#play').onclick=async()=>{const videos=[document.querySelector('#refVideo'),document.querySelector('#newVideo')];videos.forEach(v=>v.currentTime=0);await Promise.allSettled(videos.map(v=>v.play()));};
const form=document.querySelector('#feedback'),key='pixelclone-feedback-r1-v0.3';try{const previous=JSON.parse(localStorage.getItem(key)||'null');if(previous)for(const [k,v]of Object.entries(previous))if(form.elements[k])form.elements[k].value=v;}catch{}
form.oninput=()=>{try{localStorage.setItem(key,JSON.stringify(Object.fromEntries(new FormData(form))));document.querySelector('#saved').textContent='已暂存到此浏览器';}catch{}};
form.onsubmit=e=>{e.preventDefault();const f=new FormData(form),score=k=>f.get(k)===''?null:Number(f.get(k)),review={caseId:'monopo-development',round:'r1',skillVersion:'0.3.0',reviewedAt:new Date().toISOString(),humanReview:{visual:score('visual'),completion:score('completion'),motion:score('motion'),accepted:f.get('accepted'),comments:f.get('comments')}};const url=URL.createObjectURL(new Blob([JSON.stringify(review,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download='pixelclone-feedback-r1.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);document.querySelector('#saved').textContent='已导出；请在聊天中发回评价。';};
</script></html>'''
page=page.replace('STYLE',style).replace('DATA',json.dumps(evaluation,ensure_ascii=False).replace('<','\\u003c')).replace('href="../../pixelclone-skills','href="../downloads/pixelclone-skills').replace('href="../../PixelClone-Skill','href="../downloads/PixelClone-Skill')
(out/'index.html').write_text(page,encoding='utf8')
if not (root/'round-0.html').exists():shutil.copy2(root/'index.html',root/'round-0.html')
(root/'index.html').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=round-1/index.html"><title>PixelClone 第二轮</title><p><a href="round-1/index.html">打开第二轮评审</a> · <a href="round-0.html">保留的第一轮</a></p>',encoding='utf8')
for name,folders in [('pixelclone-skills-v0.3-candidate.zip',['skills']),('PixelClone-Skill-v0.3-source.zip',['skills','toolkit','tests','scripts','docs','examples','benchmarks','cases','.github'])]:
 with zipfile.ZipFile(outputs/name,'w',zipfile.ZIP_DEFLATED) as z:
  for folder in folders:
   for p in Path(folder).rglob('*'):
    if p.is_file() and not any(x in p.parts for x in ['__pycache__','node_modules','assets','vendor']):z.write(p,p.as_posix())
  if name.startswith('PixelClone'):
   for file in ['README.md','package.json','package-lock.json','requirements.txt','.gitignore']:z.write(file,file)
 with zipfile.ZipFile(outputs/name) as z:assert z.testzip() is None
 print(name,(outputs/name).stat().st_size)
 (root/'downloads').mkdir(exist_ok=True);shutil.copy2(outputs/name,root/'downloads'/name)
maxdiff=max(x['page']['ratio'] for x in comparison);mindiff=min(x['page']['ratio'] for x in comparison)
delivery=f'''# PixelClone v0.3 候选交付\n\n更新日期：2026-11-06。\n\n用户上一轮：视觉 70、完成度 60、动效 40，不接受，反馈已归档。当前评审：http://127.0.0.1:8765/round-1/index.html 。\n\n本轮独立重建了字体栅格、位移、色散、遮罩与指针驱动背景；skill 新增渲染证据合同，工具新增渲染诊断、控制台错误记录和真实触屏采集。\n\n最终桌面八个状态全页差异 {mindiff*100:.3f}%–{maxdiff*100:.3f}%，标题区域均为 0；{sum(x['withinTolerance'] for x in comparison)}/8 个状态达到全部所选区域容差。底部透镜边界、移动端关键区域仍有失败项。以上不是人眼相似度，也不是整页逐像素一致。连续运动、入场和整体接受仍待用户评价。\n\n19 项 Node、6 项 Python 测试与 9 项案例行为检查通过，双语打包同步通过。12 个独立验证案例尚未运行。当前是源码辅助开发修复，不用于宣称同条件 skill 提升或普遍成功率。\n\n安装包：pixelclone-skills-v0.3-candidate.zip；源码：PixelClone-Skill-v0.3-source.zip。案例原资源保留在本地评审目录，不包含在分发 skill 中。未推送远端、未发布、未更改全局安装。\n'''
(outputs/'DELIVERY.md').write_text(delivery,encoding='utf8');shutil.copy2('docs/ROUND-1.md',outputs/'round-1-notes.md')
print('Built review, manifest and packages')

from pathlib import Path
import zipfile,json,shutil
root=Path('.');out=Path('../outputs')
log=Path('docs/IMPLEMENTATION.md')
log.write_text(log.read_text(encoding='utf8')+'''\n## Delivery checkpoint — 2026-11-03\n\n- Toolkit: 17 Node/browser/CLI tests and 6 Python tests passed.\n- Standalone Chinese package: clean npm ci, CLI help and image collect passed.\n- Packaging parity check passed for both languages.\n- Review viewer: all three selectors, images and feedback export passed, no JavaScript errors.\n- Independent code review findings fixed with regression tests: readiness timeout, browser cleanup, static-animation metadata, delayed CSS backgrounds, source/output aliases (including junctions), duplicate case records, collapsed layout regions.\n- Three independent reconstruction trials completed; all fail faithful visual reconstruction. Candidate trial interruption and overwritten first-attempt screenshots disclosed. No claim of skill uplift.\n- Human feedback remains pending. 12 holdout cases selected; 8 pinned image inputs downloaded without inspection, 4 dynamic packages pending snapshot. No holdout runs executed.\n- Ruling: stop at concrete first-round review before tuning the frozen skill further, as the approved workflow requires the user's ratings between rounds.\n- Changes remain on local feat/pixelclone-evaluation. No push, global installation or release.\n''',encoding='utf8')
summary='''# PixelClone v0.2 候选交付\n\n完成日期：2026-11-03。源项目位于当前目录下 PixelClone-Skill，分支 feat/pixelclone-evaluation。\n\n已实现中英文 skill、图片/网页/视频采集、字体审计、截图与区域对比、布局检查、离线报告和独立安装包同步。17 项 Node 测试与 6 项 Python 测试通过；中文独立包安装与命令运行通过。GitHub Actions 配置已添加，但远端 CI 尚未运行。\n\n打开 pixelclone-review/index.html 进行首轮评价；也可通过 http://127.0.0.1:8765/index.html 访问正在运行的本地评审页。安装包为 pixelclone-skills-v0.2-candidate.zip，完整源码为 PixelClone-Skill-v0.2-source.zip。\n\n重要结论：三组 Monopo 复刻均未达到完整还原标准。新版的背景和透镜属于近似实现，严格素材规则未通过；旧版的低像素误差来自截图裁片。当前结果不能证明新 skill 的泛化提升，也不能称为像素级复刻。\n\n12 个验证案例已选定但尚未运行；4 个动态案例还未冻结参考快照。待你评价开发案例后，再更新下一轮 skill 并执行独立验证。人工分数未预填，评审页支持导出反馈。\n\n复刻稿与素材留在本地评审文件夹，仅用于本次核验。skill ZIP 不包含原站商业字体。\n'''
(out/'DELIVERY.md').write_text(summary,encoding='utf8')
shutil.copy2('docs/EVALUATION.md',out/'evaluation-summary.md')
for name,folders in [('pixelclone-skills-v0.2-candidate.zip',['skills']),('PixelClone-Skill-v0.2-source.zip',['skills','toolkit','tests','scripts','docs','examples','benchmarks','.github'])]:
 with zipfile.ZipFile(out/name,'w',zipfile.ZIP_DEFLATED) as z:
  for folder in folders:
   for p in (root/folder).rglob('*'):
    if p.is_file() and '__pycache__' not in str(p) and 'node_modules' not in str(p):z.write(p,p.as_posix())
  if name.startswith('PixelClone'):
   for f in ['README.md','package.json','package-lock.json','requirements.txt','.gitignore']:z.write(f,f)
 with zipfile.ZipFile(out/name) as z:
  assert z.testzip() is None
 print(name,(out/name).stat().st_size)

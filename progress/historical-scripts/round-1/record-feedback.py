from pathlib import Path
import json,shutil,hashlib
base=Path('../outputs/pixelclone-review')
dest=base/'round-1';dest.mkdir(exist_ok=True)
feedback={'caseId':'monopo-development','round':'r0','arm':'candidate','recordedDate':'2026-11-05','source':'User attachment and instruction in chat','humanReview':{'visual':70,'completion':60,'motion':40,'accepted':False,'comments':'整体来说视觉上的素材使用比较近似。但是详细查看字体还有ui动效会发现很大的问题，首先，字体原网页有一种失真感，复刻的网页每页体现出来，其次，ui动效复刻的是在鼠标摆动影响字体变形的特点，我们复刻的网页更像是一个mock，并没有完整的涉及到3d动效'},'interpretation':'用户要求修复原站字体失真感及鼠标驱动文字形变；截图中的“每页”保留原文，理解为未体现。'}
(dest/'feedback-r0.json').write_text(json.dumps(feedback,ensure_ascii=False,indent=2),encoding='utf8')
shutil.copy2('<LOCAL_USER>/AppData/Local/Temp/codex-clipboard-f4ac5aad-197d-4710-8b87-81e37de5320d.png',dest/'feedback-r0.png')
old=json.loads((base/'evaluation.json').read_text(encoding='utf8'))
# The original run is preserved; attach feedback separately to avoid changing its metric schema.
Path('docs/feedback').mkdir(exist_ok=True)
shutil.copy2(dest/'feedback-r0.json','docs/feedback/monopo-r0.json')
print('Recorded user review; r0 artifacts preserved')

from pathlib import Path
import shutil,json
out=Path('../outputs/pixelclone-review')
# Preserve the already captured interrupted draft; the resumed run is the final independent artifact.
shutil.copy2(out/'candidate/index.html',out/'candidate/interrupted-draft.html')
shutil.copytree('work/candidate',out/'candidate',dirs_exist_ok=True)
shutil.copy2('work/reference/stability.json',out/'reference/stability.json')
shutil.copy2('benchmarks/holdout.lock.json',out/'holdout.lock.json')

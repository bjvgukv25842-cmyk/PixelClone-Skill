import json,hashlib,urllib.request
from pathlib import Path
p=Path('benchmarks/holdout.lock.json');lock=json.loads(p.read_text());dest=Path('work/holdout-inputs');dest.mkdir(exist_ok=True)
for i,c in enumerate(lock['cases']):
 if 'dataset' in c:
  blob=urllib.request.urlopen(c['url'],timeout=40).read();f=dest/f'{i:02d}.png';f.write_bytes(blob);c['sha256']=hashlib.sha256(blob).hexdigest();c['localReference']=str(f);c['snapshotStatus']='downloaded-uninspected'
p.write_text(json.dumps(lock,indent=2),encoding='utf8');print('Locked',len(lock['cases']),'cases; downloaded 8 reference images without inspecting them.')

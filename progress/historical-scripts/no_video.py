import json
from pathlib import Path
p=Path('benchmarks/monopo.reference.json'); c=json.loads(p.read_text(encoding='utf-8-sig')); c['recordVideo']=False;p.write_text(json.dumps(c,indent=2))

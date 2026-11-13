import urllib.request,json,hashlib
from pathlib import Path
lock={'schemaVersion':1,'purpose':'held-out internal adapted evaluation; not an official leaderboard submission','lockedAt':'2026-10-29','runsExecuted':False,'cases':[]}
for ds,frameworks in [('SALT-NLP/Design2Code-HARD',None),('whale99/DesignBench',['vanilla','react','vue','angular'])]:
 data=json.load(urllib.request.urlopen('https://huggingface.co/api/datasets/'+ds)); rev=data['sha']; files=[f['rfilename'] for f in data['siblings']]
 if frameworks is None: selected=['g0.png','g20.png','g40.png','g60.png']
 else:
  selected=[]
  for f in frameworks:
   matches=sorted(p for p in files if p.startswith('generation/'+f+'/') and p.endswith('.png'))
   if not matches: print('MISSING',f);continue
   selected.append(matches[0])
 for f in selected:
  if f not in files: raise ValueError(f)
  lock['cases'].append({'id':ds.split('/')[-1]+':'+f,'dataset':ds,'revision':rev,'file':f,'url':f'https://huggingface.co/datasets/{ds}/resolve/{rev}/{f}','role':'held-out','status':'pending','inputTrack':'screenshot-only','referenceCodeAllowed':False})
for id,url,trigger in [('neutomni-preloader','https://neutomni.com/','autoplay'),('palmo-scroll','https://palmo.co.in/','scroll'),('pixel-menu','https://pixel.melbourne/','hover'),('kavieng-cards','https://kaviengcreative.com/','drag')]:
 lock['cases'].append({'id':id,'url':url,'trigger':trigger,'role':'held-out','status':'pending','inputTrack':'website-resources','snapshotStatus':'not-yet-captured','source':'https://www.physera.ai/research/animation'})
Path('benchmarks/holdout.lock.json').write_text(json.dumps(lock,ensure_ascii=False,indent=2),encoding='utf8')
print([(c['id']) for c in lock['cases']])


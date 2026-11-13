from pathlib import Path
import shutil,json
out=Path('../outputs/pixelclone-review');out.mkdir(parents=True,exist_ok=True)
for source,dest in [('work/baseline-control','control'),('work/baseline-old','old'),('work/candidate','candidate'),('work/reference','reference')]:
 shutil.copytree(source,out/dest,dirs_exist_ok=True,ignore=shutil.ignore_patterns('video','*.log'))
meta={'schemaVersion':1,'caseId':'monopo-development','status':'interrupted-independent-run','humanReview':None,'missingFeatures':['Independent new-skill agent stopped at account usage limit before QA.','Draft background paths and lens are approximations, not original shader. This conflicts with strict no-substitution acceptance and is a failed compliance finding.','Mobile reference was unavailable to all three generation arms; mobile similarity is ungraded.','Only hero and navigation scope; local lower sections are draft placeholders, not replicated routes.'],'evaluationMode':'Developer validation of interrupted draft; excluded from controlled success-rate comparison'}
(out/'candidate/notes.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf8')
print(out.resolve())

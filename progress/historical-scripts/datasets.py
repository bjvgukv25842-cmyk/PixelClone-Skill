import urllib.request,json
for name,url in [('hard','https://huggingface.co/api/datasets?search=Design2Code-HARD'),('designbench','https://huggingface.co/api/datasets?search=DesignBench')]:
 try:
  data=json.load(urllib.request.urlopen(url,timeout=20)); print(name,[(x['id']) for x in data][:10])
 except Exception as e: print(name,str(e))

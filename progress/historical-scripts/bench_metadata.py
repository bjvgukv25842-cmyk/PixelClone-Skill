import urllib.request,json
for ds in ['whale99/DesignBench','SALT-NLP/Design2Code-HARD']:
 data=json.load(urllib.request.urlopen('https://huggingface.co/api/datasets/'+ds)); print(ds,data['sha']);print([(s['rfilename']) for s in data.get('siblings',[])][:20])

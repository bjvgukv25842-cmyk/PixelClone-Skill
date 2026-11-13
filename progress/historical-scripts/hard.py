import urllib.request,json
u='https://huggingface.co/api/datasets/SALT-NLP/Design2Code-HARD/tree/main'
x=json.load(urllib.request.urlopen(u)); print([(f['path'],f.get('size')) for f in x])

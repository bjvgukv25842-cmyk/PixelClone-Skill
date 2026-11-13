import urllib.request,json
x=json.load(urllib.request.urlopen('https://huggingface.co/api/datasets/whale99/DesignBench'))
print(sorted(set('/'.join(s['rfilename'].split('/')[:2]) for s in x['siblings'] if s['rfilename'].startswith('generation/'))))

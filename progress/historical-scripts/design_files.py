import urllib.request,json
x=json.load(urllib.request.urlopen('https://huggingface.co/api/datasets/whale99/DesignBench'))
files=[s['rfilename'] for s in x['siblings']]
print('\n'.join(files[-70:]));print('roots',sorted(set(p.split('/')[0] for p in files)))

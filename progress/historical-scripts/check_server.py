import urllib.request,subprocess
try: print(urllib.request.urlopen('http://127.0.0.1:8765/index.html',timeout=3).status)
except Exception: print('SERVER_NOT_READY')

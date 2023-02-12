import requests

r = requests.post("http://127.0.0.1:8000/api/plugincheck/check/testplugin2", data={"key": "WRRPWUED-AGTRG42N-J3DOZ39N-3U1XTOC3"})
print(r.text)
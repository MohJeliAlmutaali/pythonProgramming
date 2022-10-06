import m3u8
import requests

url = "https://manifest.prod.boltdns.net/manifest/v1/hls/v4/clear/3588749423001/d5771d5d-a702-49f5-899e-c92cd22d7901/10s/master.m3u8?fastly_token=NjMzNmE1YTRfYmQ2MTMxNjE3NTUxMzBjYTA2MmIwNGJmNDUwY2Q0NzAyNTYzY2QwZWFmMGMzN2I0NTcxYmEzMDc1MjgxNjM0NQ%3D%3D"

r = requests.get(url)
print(r.text)

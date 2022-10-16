import requests
import json

header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Cookie":"BAIDUID=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; BAIDUID_BFESS=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1665934930; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1665934930; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1665934930; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1665934930; ab_sr=1.0.1_ODg2M2Q4OThhODI4OWFlNzRkMGE1MjkwNmZlNGQwMWIyZTBiOTA3YTE5ZGM4NGYxMjVkYjQyYjE3OGY5OTdlODJiMGI1MTM4YzQ2OWIxMjJlNTY3MGU4ODg2NDU2ZjA4MDU0Mzg0YzM1YzhkNzA1OTM3YWI1ZWMxY2EzYTQ1MzFiMGM0MmU1ZWI1NzJkM2YwYmNkOGViOGJmYTVlMjdmMg=="

}
data = {
    "query": "你是谁",
    "from": "zh",
    "to": "en",
    "token": "c98deb750bb7b61af68262082d7edada",
    "sign": "637195.875066"
}

post_url = "https://fanyi.baidu.com/basetrans"

r = requests.post(post_url, data=data, headers=header)

print(r.content.decode())
dict = json.loads(r.content.decode())
recv = dict["trans"][0]["dst"]
print("翻译结果:%s" % recv)

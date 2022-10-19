
import requests
import json
import parsel
url = "https://movie.douban.com/top250"

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"}
respose = requests.get(url,headers=headers)

ret_html = respose.text
with open("ret.html","w",encoding="utf-8") as f:
    f.write(ret_html)

selector = parsel.Selector(ret_html)
moviename = selector.css('.item')
print(moviename)
# with open("douban.json","w",encoding="utf-8") as f:
#     f.write(recv)
#
#
#
# with open("douban.json","r",encoding="utf-8") as f:
#     ret = json.dumps(f.read())


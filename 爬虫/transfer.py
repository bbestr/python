
import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
data = {
"from": "en",
"to": "zh",
"query": "hi",
"simple_means_flag": "3",
"sign": "742533.1030068",
"token": "1967e7c6721c151b384827b0b06396a3",
"domain": "common"
}

post_url = "https://fanyi.baidu.com/v2transapi"

r = requests.post(post_url,data=data,headers=header)

print(r.content.decode())
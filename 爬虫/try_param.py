# coding=utf-8
import requests


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}


for i in range(0,20):
    url_temp = "https://tieba.baidu.com/f?kw={}&ie={}&pn={}".format("rng","utf-8",i*50)
    respose = requests.get(url_temp,headers = header)
    print(respose.request.url)

print(respose.status_code)


import requests
import json

proxy = {"http":"http://188.131.233.175:8118"}
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
respose = requests.get("https://www.baidu.com",proxies = proxy,headers = header)

print(respose.status_code)
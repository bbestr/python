# coding=utf-8
import requests
import json
session = requests.session()

post_url = "https://mail.qq.com/"

post_data = {"2246368209":"mlj.2000."}

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
session.post(post_url,data=post_data,headers=header)


respose = session.get("https://mail.qq.com/cgi-bin/frame_html",headers=header)

r = json.load(respose.content.decode())
print(r)


import requests

respose = requests.get("https://p3.ssl.qhimgs1.com/t01d8a77d9e5fe8500d.jpg")



with open("a.jpg","wb") as f:
    f.write(respose.content)
import requests
from bs4 import BeautifulSoup
def main():

    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    response = requests.get("http://www.baidu.com",headers = header)

    code = response.status_code

    print(response.headers)
    ret = response.content.decode()
    type(ret)
    with open("1.html","w",encoding="utf-8") as f:
        f.write(ret)
    soup = BeautifulSoup(open("1.html"))
    print(soup.prettify())

if __name__ == '__main__':
    main()
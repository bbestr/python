import requests

def main():

    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    response = requests.get("http://www.baidu.com",headers = header)

    code = response.status_code
    print(code)

    print(response.headers)
    print(response.content.decode())

if __name__ == '__main__':
    main()
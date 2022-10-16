import requests


class Tieba:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + self.tieba_name + "&ie=utf-8&pn={}"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    def get_url_list(self):
        """构造url列表"""
        # url_list = []
        # for i in range(50):
        #   url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i * 50) for i in range(20)]

    def parse_url(self, url):
        """发送请求"""
        print(url)
        response = requests.get(url, self.header)
        return response.content.decode("utf-8")

    def save_html(self, html_temp, pageno):
        """保存爬的页面"""
        file_path = "{}--第{}页.html".format(self.tieba_name, pageno)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_temp)

    def run(self):
        temp_list = self.get_url_list()
        for li in temp_list:
            html = self.parse_url(li)
            pageno = temp_list.index(li) + 1
            self.save_html(html, pageno)


if __name__ == '__main__':
    tieba = Tieba("rng")
    tieba.run()

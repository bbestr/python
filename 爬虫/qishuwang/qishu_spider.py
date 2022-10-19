import requests
from bs4 import BeautifulSoup
import json
import re


class QiShuPaChong:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            "Cookie": "BAIDUID=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; BAIDUID_BFESS=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1665934930,1665971726; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1665934930,1665971760; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1666012639; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1666012639; ab_sr=1.0.1_NDk0NWFjNjJmYmEzOGMwN2M2MzZjMmQ5YTcwNDA1MDA1ZTkxNjI2MTgwYTA5NmY2Nzc1ZDBjYTBiZGEwZTYxOTA5ZDJiN2IyOGUxN2Q2ZDZiZDNlNzUyZWJjMWJmOWE0NTJhNTVmNjk3MDhlMGY2NjM2YjJiMmEwMTkwYWQwZDVlMzNjMzc5NjRhZTcwNzIyN2E3ODlkMDEwZTFjNWM2OA=="}
        self.url1 = "soft/sort01/"
        self.url = "https://www.qishuta.la/"
        self.temp_url = []
        self.lastdata = []

    def parse_url(self, url):
        """发送请求"""
        main_url = requests.post(url, headers=self.headers)
        print(main_url.status_code)
        self.temp_html = main_url.content.decode()
        self.save_html()

    def url_link(self, tempurl):
        """url 拼接"""
        return self.url + tempurl

    def save_html(self):
        """保存html 数据"""
        with open("temp.html", "w", encoding="utf-8") as f:
            f.write(self.temp_html)

    def run(self):
        # 发送请求
        self.lenth = 15
        self.pageno = 0
        while self.lenth == 15:
            if self.pageno == 0:
                self.parse_url(self.url+self.url1)
            else:
                index = "index_"+str(self.pageno)+".html"
                self.parse_url(self.url + self.url1+index)
            # 解析html获取分类url  拼接url 进入分类模块
            soup = BeautifulSoup(open("temp.html", "rb"), 'lxml')
            liTags = soup.find_all("a")
            print(liTags)
            temp_url =[]
            for li in liTags:
                self.temp = li.get('href')[1:].replace("\n", " ").strip()
                ss = str(li)
                if len(self.temp) == 0:
                    continue
                elif self.temp[0] == 'S' and len(ss) > 80:
                    temp_url.append(self.temp)
                else:
                    continue
            print("------------------------------------")
            self.lenth = len(temp_url) #保存当前页面  书籍数量  如果不足一页则说明 爬完了
            print(len(temp_url))
            for par in temp_url:
                fina_url = self.url + par
                print("------------------------")
                print("最终url是:",fina_url)
                respo = requests.get(fina_url, headers=self.headers)
                print("状态码:", respo.status_code)
                ret = respo.content.decode()
                print("写入文件中--")
                with open("fina.html","w",encoding="utf-8") as f:
                    f.write(ret)

                print("写完一个文件")

                print("----------------")
                print("开始解析")
                # 解析获取具体书籍下载页面
                soup1 = BeautifulSoup(open("fina.html", "rb"), 'lxml')
                liTags1 = soup1.find_all('script')
                for li1 in liTags1:
                    li1 = str(li1)
                    if len(li1) == 0:
                        continue
                    else:
                        if li1[-12:][0] == "'":
                            a1 = li1[44:-12].replace("'", "")
                            d = a1.split(",")
                            # 解析页面  获取下载链接
                            # 保存数据
                            print(d)
                            with open("qushu1.txt","a",encoding="utf-8") as f:
                                f.write("书名:<<"+d[2]+">>:")
                                f.write("  下载链接:"+d[1]+"  ")
                                f.write("  在线观看:"+self.url+d[0])
                                f.write("\n")
            self.pageno += 1

if __name__ == '__main__':
    # 1       2        3        4       5        6       7        8        9      10
    # 玄幻    武侠       言情      都市   军事   电竞       科幻      没问    剧本    名著
    qishu = QiShuPaChong()
    qishu.run()

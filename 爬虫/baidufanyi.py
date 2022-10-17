from get_sign import *
import requests
import json

class BaiduFanyi:
    def __init__(self,transdata,sign):
        self.lan_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_data = transdata
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.sign = sign
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
                        "Cookie": "BAIDUID=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; BAIDUID_BFESS=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1665934930,1665971726; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1665934930,1665971760; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1666012639; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1666012639; ab_sr=1.0.1_NDk0NWFjNjJmYmEzOGMwN2M2MzZjMmQ5YTcwNDA1MDA1ZTkxNjI2MTgwYTA5NmY2Nzc1ZDBjYTBiZGEwZTYxOTA5ZDJiN2IyOGUxN2Q2ZDZiZDNlNzUyZWJjMWJmOWE0NTJhNTVmNjk3MDhlMGY2NjM2YjJiMmEwMTkwYWQwZDVlMzNjMzc5NjRhZTcwNzIyN2E3ODlkMDEwZTFjNWM2OA=="}
    def parse_url(self,url,data):
        respose = requests.post(url,data=data,headers=self.headers)
        hh = json.loads(respose.content.decode())
        return hh

    def run(self):

        #获取语言累心
        post_data = {"query":self.trans_data}
        language = self.parse_url(self.lan_detect_url,post_data)['lan']

        #准备post 数据
        trans_data_1 = {"query": self.trans_data,"from": "zh","to": "en","token": "c98deb750bb7b61af68262082d7edada","sign": self.sign} if language == "zh" else \
            {"query": self.trans_data,"from": "en","to": "zh","token": "c98deb750bb7b61af68262082d7edada","sign": self.sign}
        #发送请求 获取相应
        recv = self.parse_url(self.trans_url,trans_data_1)
        print("------")
        self.get_result(recv)

        #提取翻译结果
    def get_result(self,recv):
        self.ret = recv["trans"][0]["dst"]
        print("翻译结果:",self.ret)

if __name__ == '__main__':

    transdata = input("请输入翻译信息:")
    sign_temp = sign(transdata)
    baidufanyi = BaiduFanyi(transdata,sign_temp)
    baidufanyi.run()
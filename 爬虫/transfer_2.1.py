import requests
import json

class Translate:
    def __init__(self):

        self.url = "https://fanyi.baidu.com/basetrans"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
            "Cookie":"BAIDUID=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; BAIDUID_BFESS=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1665934930,1665971726; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1665971760; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1665934930,1665971760; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1665971760; ab_sr=1.0.1_ZTJmNDE4NzBjZjc5ZjlkZDBkZTk3ZGRhYzA4YjQwNjBmNjJiMTFmMzZlMDJiMDIzNTMwNmQ2MTFkODRjZTE1NTQ4ODIzZGE1YzQ0MGM0MTc2MWFiNzRkYjdhZTc5ZjRiZDE4ZjRjNjZhZmIwNjUxMDFhMjZkZTkwMTQ4MTE0Y2VmNmRjMDMwZmY2OWYxYjdjOTg3NWEzNDgzOWRjZWRkYg=="

        }
        self.data = {
            "query": None,
            "from": "zh",
            "to": "en",
            "token": "c98deb750bb7b61af68262082d7edada",
            "sign": "637195.875066"
        }

    def get_fanyi_sign(self):
        with open("baidusign.js") as f:
            jsdata =f.read()
        return jsdata


    def get_result(self):
        self.result = json.loads(self.r.content.decode())
        self.recv = self.result["trans"][0]["dst"]
        print("翻译结果 %s" % self.recv)


    def run(self):
        #获取 输入 信息
        self.shuru = input("输入想翻译的内容: ")
        self.data["query"] = self.shuru
        # 获取 sign值  一并装入data

        # sign_temp = self.get_fanyi_sign()
        # print(sign_temp)
        # self.data["sign"] = sign_temp

        #requests post 请求
        self.r = requests.post(self.url, data=self.data, headers=self.header)

        #返回 翻译结果
if __name__ == '__main__':
    fanyi = Translate()
    fanyi.run()
    fanyi.get_result()

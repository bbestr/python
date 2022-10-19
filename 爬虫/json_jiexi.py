import json
import requests

# 1.请求json接口整体数据
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
                        "Cookie": "BAIDUID=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; BAIDUID_BFESS=5695F9D405A926CB4C37CD9EFFFA4AD9:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1665934930,1665971726; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1665934930,1665971760; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1666012639; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1666012639; ab_sr=1.0.1_NDk0NWFjNjJmYmEzOGMwN2M2MzZjMmQ5YTcwNDA1MDA1ZTkxNjI2MTgwYTA5NmY2Nzc1ZDBjYTBiZGEwZTYxOTA5ZDJiN2IyOGUxN2Q2ZDZiZDNlNzUyZWJjMWJmOWE0NTJhNTVmNjk3MDhlMGY2NjM2YjJiMmEwMTkwYWQwZDVlMzNjMzc5NjRhZTcwNzIyN2E3ODlkMDEwZTFjNWM2OA=="}
response = requests.get("https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=250",headers=headers)


# 2.抽取想要的数据

py_data = json.loads(response.content.decode())  # 将已编码的 JSON 字符串解码为 Python 对象
#查看数据类型  字典类型
for i in py_data:
    items = {"电影名称": i['title'], "上映时间": i['release_date'], "上映地区": i['regions'], "影片评分": i['score'],
             "影片类型": i['types']}

    content = json.dumps(items, ensure_ascii=False)
    print(content)

    # 3.保存数据
    # 设置编码方式，防止乱码
    with open("douban.json", "a", encoding="utf-8")as f:
        f.write(content)


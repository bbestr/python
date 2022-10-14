class Tools:
    count = 0
    def __init__(self,name):
        self.name = name
        Tools.count += 1
    @classmethod
    def count_jishu(cls):
        print("数量为%d" %cls.count)
futou = Tools("FUTOU")
hah = Tools("DWADA")
Tools.count_jishu()
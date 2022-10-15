class Tools:
    count = 0
    def __init__(self,name):
        self.name = name
        Tools.count += 1
futou  = Tools("futou")
print(Tools.count)
print(futou.count)
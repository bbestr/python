class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "家具%s占地%s"%(self.name,self.area)

class House:
    def __init__(self,type,area):
        self.type = type
        self.area = area
        self.free_area = area
        self.item = []
    def __str__(self):
        return "户型:%s\n总面积:%s[剩余面积:%s]\n家具:%s"%(self.type,self.area,self.free_area,self.item)
    def add_iitem(self,item):
        if item.area > self.free_area:
            print("家具太大:放不下了")
            return
        self.item.append(item.name)
        self.free_area  -= item.area
yigui = HouseItem("衣柜",30)
dianshi = HouseItem("电视",2)
bingxiang = HouseItem("冰箱",1)
print(yigui)
print(dianshi)
print(bingxiang)


myhouse = House("三室一厅",80)
myhouse.add_iitem(yigui)
myhouse.add_iitem(dianshi)
myhouse.add_iitem(bingxiang)
print(myhouse)
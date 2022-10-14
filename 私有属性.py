#大大
class Women:
    def __init__(self,name):
        self.name = name
        self.__weight = 50
    def __secret(self):
        print("%s 和%d" % (self.name,self.__weight))
xiaohong = Women("晓东")
print(xiaohong._Women__secret())
print("789")
print(xiaohong._Women__weight)


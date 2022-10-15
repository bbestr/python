class Cat:

    def __init__(self,name):
        self.name = name
    def eat(self):
        print("%s吃饭中" %self.name)
    @staticmethod
    def drink():
        print("喝水中")

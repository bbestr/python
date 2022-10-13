class Cat:
    def __init__(self,name_ok):
        print("初始化方法")
        self.name = name_ok
tom = Cat("汤姆吗")
print(tom.name)
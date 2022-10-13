class Cat:
    def eat(self):
        print("%s吃饭中" %self.name)
    def drink(self):
        print("喝水中")
tom = Cat()
tom.name = "加菲猫"
tom.eat()
tom.drink()
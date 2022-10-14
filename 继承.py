class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def sleep(self):
        print("谁")
    def run(self):
        print("跑")
class Wangcai(Animal):
    def bark(self):
        print("bak")
class Xiaotianquan(Wangcai):
    def fly(self):
        print("飞")
    def bark(self):
        super().bark()
        print("哮天犬  旺旺")
wangcai = Wangcai()
wangcai.eat()
wangcai.bark()
wangcai.sleep()
wangcai.run()
wangcai.drink()
xiaotian = Xiaotianquan()
xiaotian.bark()
xiaotian.fly()
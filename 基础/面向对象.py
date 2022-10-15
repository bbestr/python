class Persoon:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def run(self):
        print("跑步")
        self.weight -= 1
    def eat(self):
        print("吃东西")
        self.weight += 1
    def __str__(self):
        return "我的名字叫%s,体重是%.2f" %(self.name,self.weight)
xiaomin = Persoon("xiaoming",56.368)
xiaomin.run()
xiaomin.eat()
print(xiaomin)
class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None
    def fire(self):
        if self.gun:
            if self.gun.bullet == 0:
                print("没子弹! 请装弹")
                self.gun.add_bullet(10)
                print("正在装弹")
                print("开火")
                self.gun.shoot()
            else:
                self.gun.shoot()

class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet = 0
    def add_bullet(self,count):
        self.bullet += count
    def shoot(self):
        if self.bullet == 0:
            print("没子弹!")
        else:
            print("发射子弹")
            self.bullet -= 1
            print("- "*5)
        print("%s还剩%s课子弹"%(self.model,self.bullet))
ak = Gun("AK-47")
xusanduo = Soldier("卢锡安")
xusanduo.gun = ak
xusanduo.fire()

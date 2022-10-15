class Game:
    mo = None
    def __init__(self):
        print("初始化")
    def __new__(cls, *args, **kwargs):
        if cls.mo is None:
            cls.mo = super().__new__(cls)
        return cls.mo
p1 = Game()
print(p1)
p2 = Game()
print(p2)

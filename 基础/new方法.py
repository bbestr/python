class Music:
    def __new__(cls, *args, **kwargs):
        print("创建new  分配空间")
        return super().__new__(cls)
    def __init__(self):
        print("初始化")
nn = Music()

class Game:
    top_score = 0
    def __init__(self,name):
        self.name = name
    @staticmethod
    def show_help():
        print("右手就行吧! 没什么好说的")
    @classmethod
    def show_top_socre(cls):
        print("最高分为%d"%cls.top_score)
    def strat_game(self):
        print("玩家%s开始游戏"%self.name)
Game.show_help()
Game.show_top_socre()
xiaoming = Game("best")

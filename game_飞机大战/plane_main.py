import pygame
from plane_sprite import *

FRAME_SEC = 60
CREATE_ENEMY = pygame.USEREVENT
SCREEN_R = pygame.Rect(0,0,480,700)
ENEMY_MODEL = pygame.Rect(0,0,53,43)
class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")

        #创建游戏窗口
        self.screen = pygame.display.set_mode((SCREEN_R.width,SCREEN_R.height))

        #创建游戏时钟
        self.clock = pygame.time.Clock()


        #创建精灵组
        self.__create_sprites()


        #创建定时器 创建敌人
        pygame.time.set_timer(CREATE_ENEMY,1000)
    def __create_sprites(self):
        """创建精灵"""
        bg1 = background(False)
        bg2 = background()
        self.background = pygame.sprite.Group(bg1,bg2)

        self.enemy_group = pygame.sprite.Group()

    def start_game(self):
        print("游戏开始")
        while True:
            #设置刷新率
            self.clock.tick(FRAME_SEC)
            #事件监听
            self.__event_hander()
            #碰撞检测
            self.__check_collide()
            #更新绘制 精灵
            self.__updatesprite()
            #更新显示
            pygame.display.update()
            pass
    def __event_hander(self):
        """时间解控"""
        for even in pygame.event.get():
            if even.type == pygame.QUIT:  # 退出程序
                PlaneGame.__gameover()

            elif even.type == CREATE_ENEMY:

                enemy1 = enmey_create()
                self.enemy_group.add(enemy1)


    def __check_collide(self):
        """碰撞检测"""

    def __updatesprite(self):
        """更新精灵组"""
        self.background.update()
        self.background.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __gameover():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
import pygame
from plane_sprite import *

pygame.init()
#屏幕
screen = pygame.display.set_mode((480,700))

#背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

#玩家战斗机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))

#更新屏幕
pygame.display.update()
#时钟对象
clock = pygame.time.Clock()

#战斗机 初始位置
hero_ract = pygame.Rect(200,500,102,126)

#创建敌人 精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)
#创建精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)
while True:
    clock.tick(20)
    #监听事件
    for even in pygame.event.get():
        if even.type == pygame.QUIT:#退出程序
            pygame.quit()
            exit()

    #修改飞机位置
    hero_ract.y -= 50

    #判断是否飞出界面
    if (hero_ract.y+hero_ract.height) <= 0:
        hero_ract.y = 700
    #调用bilt 绘制图像
    screen.blit(bg,(0,0)) #每次更新背景覆盖 战斗机更新
    screen.blit(hero,hero_ract)
    #让精灵调用pygame方法
    enemy_group.update()

    #在screen 上绘制
    enemy_group.draw(screen)
    #update更新
    pygame.display.update()

pygame.quit()




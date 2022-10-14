import pygame
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
while True:
    clock.tick(60)
    #修改飞机位置
    hero_ract.y -= 50
    #调用bilt 绘制凸显
    screen.blit(hero,hero_ract)
    #update更新
    pygame.display.update()

pygame.quit()




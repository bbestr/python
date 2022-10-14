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

i= 0
while True:
    clock.tick(60)
    i += 1
    print(i)
    pass

pygame.quit()




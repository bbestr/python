import pygame
import random

FRAME_SEC = 60
CREATE_ENEMY = pygame.USEREVENT
SCREEN_R = pygame.Rect(0, 0, 480, 700)
ENEMY_MODEL = pygame.Rect(0, 0, 53, 43)
HREO_FIRE = pygame.USEREVENT +1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战 飞机精灵"""

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.speed = speed
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed


class background(GameSprite):
    """"游戏背景"""

    def __init__(self, alt=True):
        super().__init__("./images/background.png")
        self.alt = alt
        if self.alt:
            self.rect.y = -SCREEN_R.height

    def update(self):
        # 1.调用父类
        super().update()
        # 2. 判断背景
        if self.rect.y >= SCREEN_R.height:
            self.rect.y = -SCREEN_R.height


class enmey_create(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")

        self.speed = random.randint(1, 3)
        self.rect.y = -ENEMY_MODEL.height
        self.rect.x = random.randint(0, SCREEN_R.width - ENEMY_MODEL.width)

    def update(self):
        super().update()
        if self.rect.y >= 700:
            self.kill()


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_R.centerx
        self.rect.bottom = SCREEN_R.height - 120
        # 创建子弹
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_R.width:
            self.rect.right = SCREEN_R.width
    def fire(self):
        #创建子弹
        for i in range(0,1,2):
            bullet = Bullet()
            #初始化子单位之
            bullet.rect.bottom = self.rect.y - (i*20)
            bullet.rect.centerx = self.rect.centerx
            #将子弹添加入 group
            self.bullet_group.add(bullet)
class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png")
        self.speed = -1

    def update(self):
        super().update()
        #子弹发射 更新位置
        self.rect.y += self.speed

        #超出屏幕删除
        if self.rect.bottom < 0:
            self.kill()

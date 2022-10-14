import pygame
import random
from plane_main import *

class GameSprite(pygame.sprite.Sprite):
    """飞机大战 飞机精灵"""
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.speed = speed
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += self.speed
class background(GameSprite):
     """"游戏背景"""
     def __init__(self,alt = True):
         super().__init__("./images/background.png")
         self.alt = alt
         if self.alt:
             self.rect.y = -SCREEN_R.height
     def update(self):
        #1.调用父类
        super().update()
        #2. 判断背景
        if self.rect.y >= SCREEN_R.height:
            self.rect.y = -SCREEN_R.height
class enmey_create(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")

        self.speed = random.randint(1,3)
        self.rect.y = -ENEMY_MODEL.height
        self.rect.x = random.randint(0,SCREEN_R.width -ENEMY_MODEL.width)
    def update(self):
        super().update()
        if self.rect.y >= 700:
            self.kill()


import pygame, sys
from pygame.locals import *
from random import *
import random
from FlyConstants import *
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/enemy1.png').convert_alpha()
        self.destory_images = []
        self.destory_images.extend([ \
            pygame.image.load('images/enemy1_down1.png').convert_alpha(), \
            pygame.image.load('images/enemy1_down2.png').convert_alpha(), \
            pygame.image.load('images/enemy1_down3.png').convert_alpha(), \
            pygame.image.load('images/enemy1_down4.png').convert_alpha() \
            ])
        self.width, self.height = BACK_GROUND_SIZE[0], BACK_GROUND_SIZE[1]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)
        self.speed = 2
        self.active = True
        # 飞机碰撞检测，会忽略掉图片中白色的背景部分
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        print(self.rect.center)
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > self.height):
            self.rect.top = 0
            self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)





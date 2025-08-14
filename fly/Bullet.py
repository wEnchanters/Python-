import pygame, sys
from pygame.locals import *
from FlyConstants import *
from Player import *
class Bullet(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pygame.image.load("images/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.center = tuple(center)
    def move(self):
        self.rect.move_ip(0, -5)



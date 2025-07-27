import pygame, sys
from pygame.locals import *
from FlyConstants import *
from Bullet import *

bulletGroup = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = PLAYER_IMAGE_FILE
        self.rect = self.image.get_rect()
        self.rect.center = (INITIAL_X, INITIAL_Y)

    def move(self):

        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

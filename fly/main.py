# Imports
import pygame, sys
from pygame.locals import *
from FlyConstants import *
import random, time
from Player import *
from Enemy import *
from Bullet import *


# Initialzing
pygame.init()
# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

def add_small_enemies(group1 : pygame.sprite.Group, group2 : pygame.sprite.Group, num : int):
    for i in range(num):
        e1 = enemy.SmallEnemy(BACK_GROUND_SIZE)
        group1.add(e1)
        group2.add(e1)

# Create a white screen
DISPLAYSURF = pygame.display.set_mode(BACK_GROUND_SIZE)
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption(CAPTION)

# Setting up Sprites
P1 = Player()
E1 = SmallEnemy()
bulletGroup = pygame.sprite.Group()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)


# Game Loop
while True:
    DISPLAYSURF.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            # 监听按键按下事件
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)  # 获取按下键的名称
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_SPACE]:
                bullet = Bullet(P1.rect.midtop)
                bulletGroup.add(bullet)
    print(all_sprites.__len__())

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    for enemy in enemies:

        if pygame.sprite.spritecollideany(enemy, bulletGroup):
            pygame.display.update()
            enemy.kill()

    for item in bulletGroup:
        item.move()
        DISPLAYSURF.blit(item.image, item.rect)
    pygame.display.update()
    FramePerSec.tick(FPS)# Imports


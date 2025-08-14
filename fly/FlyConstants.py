import pygame, sys
from pygame.locals import *



# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
BACK_GROUND_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SPEED = 5
SCORE = 0
INITIAL_X = 160
INITIAL_Y = 520

# import os
#
# image_path = os.path.join("images", "me1.png")
# if not os.path.exists(image_path):
#     print(f"❌ 错误：图片不存在！路径: {image_path}")
# else:
#     background = pygame.image.load(image_path)
#     print("✅ 图片加载成功！")

background = pygame.image.load("images/background.png")
PLAYER_IMAGE_FILE = pygame.image.load("images/me1.png")
ENEMY_ONE_IMAGE_FILE = pygame.image.load("images/enemy1.png")
ENEMY_TWO_IMAGE_FILE = pygame.image.load("images/enemy2.png")
ENEMY_THREE_IMAGE_FILE = pygame.image.load("images/enemy3_n1.png")

CAPTION = "Fly Figh"


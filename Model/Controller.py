import pygame
from Model.MySprite import MySprite
from constants import *
from Model.Plant import *
from pygame.locals import *
import sys, time
# 游戏的初始化
pygame.init()

# 创建游戏主窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 创建时钟对象 (可以控制游戏循环频率)
clock = pygame.time.Clock()
while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    a= SunFlower(100,200)
    spriteGroup=pygame.sprite.Group()
    spriteGroup.add(a.sprite)
    spriteGroup.draw(screen)
    pygame.display.update()
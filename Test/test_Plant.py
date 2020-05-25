from unittest import TestCase
from Model.Plant import *
import sys, time, random, math, pygame
from pygame.locals import *

class TestPlant(TestCase):
    def test_beattacked(self):
        self.fail()

    def test_get_sprite(self):
        self.fail()

    def test_something(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        # 设置游戏帧数
        framerate = pygame.time.Clock()
        font = pygame.font.Font(None, 18)
        fps=20
        # 创建两个精灵组
        group_plants = pygame.sprite.Group()
        group_zombies = pygame.sprite.Group()
        group_bullets = pygame.sprite.Group()
        pea1=PeaShooter(100,200)
        sun1=SunFlower(600,200)
        group_plants.add(pea1)
        group_plants.add(sun1)
        group_bullets.add(pea1.bullet)
        while True:
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            if pygame.sprite.collide_rect_ratio( 0.5 )(pea1.bullet, sun1):
                pea1.bullet.boom()
            group_plants.update()
            group_bullets.update()
            group_plants.draw(screen)
            group_bullets.draw(screen)
            pygame.display.update()
            framerate.tick(fps)





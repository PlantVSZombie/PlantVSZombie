from unittest import TestCase

import pygame

from Model import Menubar, Controller
from Model.Sun import Sun


class TestSun(TestCase):
    def test_something(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("测试卡片")
        map = pygame.image.load('../resources/pics/items/Background_0.jpg')

        menu = Menubar.Menubar(10, 10, [0, 1], 200)
        menu.draw(screen)

        sun = Sun(200, 0)
        sun.SetLineDestination(200)  # 直线下降

        sun2 = Sun(200, 200)
        sun2.SetArcDestination(250, 200)  # 斜着跑

        while True:
            screen.blit(map, (0, 0))

            x, y = pygame.mouse.get_pos()
            mouse_click, _, _ = pygame.mouse.get_pressed()
            Controller.dealCardSelected((x, y), mouse_click, menu)  # 调用Controller类的管理函数
            menu.update(menu.sun_value, pygame.time.get_ticks())
            menu.draw(screen)

            sun.update()
            if sun.isAlive():
                sun.draw(screen)
                if sun.isClicked(mouse_click, (x, y)):
                    print("阳光+10")

            sun2.update()
            if sun2.isAlive():
                sun2.draw(screen)
                if sun2.isClicked(mouse_click, (x, y)):
                    print("阳光+10")

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

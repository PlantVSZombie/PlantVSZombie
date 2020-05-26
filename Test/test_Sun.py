from unittest import TestCase

import pygame

from Model.Sun import Sun


class TestSun(TestCase):
    def test_something(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("测试卡片")
        map = pygame.image.load('../resources/pics/items/Background_0.jpg')
        block = pygame.time.Clock()


        sun = Sun(200, 0)
        sun.SetLineDestination(200)  # 直线下降

        sun2 = Sun(200, 200,7)
        sun2.SetArcDestination(250, 260)  # 斜着跑

        while True:
            block.tick(15)
            screen.blit(map, (0, 0))

            x, y = pygame.mouse.get_pos()
            mouse_click, _, _ = pygame.mouse.get_pressed()

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

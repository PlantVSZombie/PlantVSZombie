from unittest import TestCase

import pygame

from Model.Car import Car


class TestCar(TestCase):
    def setUp(self) -> None:
        pass
    def test_something(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("测试小车")
        # 设置游戏帧数
        framerate = pygame.time.Clock()
        font = pygame.font.Font(None, 18)

        car=Car(100,100)
        cars=pygame.sprite.Group()
        cars.add(car)

        while True:
            screen.fill([255, 255, 255])
            car.move()
            car.update()
            screen.blit(car.image,car.rect)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

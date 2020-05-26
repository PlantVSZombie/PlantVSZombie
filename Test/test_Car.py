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

        cars = []
        for i in range(5):
            car = Car.CreateCarAtRow(i) #第i行的车
            cars.append(car)

        while True:
            screen.fill([255, 255, 255])
            for car in cars:
                #car.move() #向前移动一点
                car.update() #更新状态
                screen.blit(car.image,car.rect) #画图

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

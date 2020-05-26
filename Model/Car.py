from enum import Enum

import pygame

from Model.MySprite import MySprite
from constants import PIC_CAR_PATH


class CarState(Enum):
    STATIC = 1  # 静止状态
    MOVING = 2


class Car(MySprite):

    def __init__(self, posx, posy):
        carimg = pygame.image.load("../" + PIC_CAR_PATH).convert_alpha()

        super().__init__(carimg)
        self.position = posx, posy

        self._state = CarState.STATIC

        self.speed = 1

    def move(self):
        self._state = CarState.MOVING

    def isMoving(self):
        return self._state == CarState.MOVING

    def update(self):
        # super.update(self)
        if self._state == CarState.STATIC:
            pass
        elif self._state == CarState.MOVING:
            self.X += self.speed

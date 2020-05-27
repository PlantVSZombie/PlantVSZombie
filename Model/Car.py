from enum import Enum

import pygame

from Model.MySprite import MySprite
from Model.Zone import Zone
from constants import PIC_CAR_PATH

SCREEN_WIDTH = 1000
CAR_SPEED = 10
class CarState(Enum):
    STATIC = 1  # 静止状态
    MOVING = 2
    RUN_OUT_SCREEN = 3 #跑出屏幕


class Car(MySprite):

    def __init__(self, posx, posy,row):
        carimg = pygame.image.load("../" + PIC_CAR_PATH).convert_alpha()
        self.row = row
        super().__init__(carimg)
        self.position = posx, posy

        self._state = CarState.STATIC


    @classmethod
    def CreateCarAtRow(cls, y):
        z = Zone()
        return Car(z.getGridPos(0, y)[0]-60, z.getGridPos(0, y)[1],y)

    def isRUN_OUT_SCREEN(self):
        return self._state == CarState.RUN_OUT_SCREEN

    def update(self):
        # super.update(self)
        if self._state == CarState.STATIC:
            pass
        elif self._state == CarState.MOVING:
            self.X += CAR_SPEED
            if self.X > SCREEN_WIDTH:
                self._state = CarState.RUN_OUT_SCREEN

    def check(self,enemyList):
        for enemy in enemyList:
            if pygame.sprite.collide_circle_ratio(0.5)(enemy,self):
                self._state = CarState.MOVING
                enemy.setDamage(9999)

    def draw(self, screen):
        if self._state != CarState.RUN_OUT_SCREEN:
            screen.blit(self.image, self.rect)



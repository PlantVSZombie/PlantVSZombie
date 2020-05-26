from enum import Enum

import pygame

from Model.MySprite import MySprite
from constants import PIC_SUN_PATH, PIC_SUN_PATH_NUM


class SunState(Enum):
    HIDE = 0
    STATIC = 1  # 静止状态
    MOVING = 2
class Sun(MySprite):

    def __init__(self, posx, posy):
        carimg = [pygame.image.load("../" + PIC_SUN_PATH.format(i) for i in range(PIC_SUN_PATH_NUM)).convert_alpha()]

        super().__init__(carimg)
        self.position = posx, posy

        self._state = SunState.HIDE

        self.pic_index = 1
        self.left_time=1000 #剩余时间
        self.destion = [0,0]

    def move(self,dest_x,dest_y):
        self._state = SunState.MOVING
        self.destion = [dest_x,dest_y]

    def isMoving(self):
        return self._state == SunState.MOVING

    def update(self):
        # super.update(self)
        if self._state == SunState.STATIC:
            pass
        elif self._state == SunState.MOVING:
            self.Y += 1
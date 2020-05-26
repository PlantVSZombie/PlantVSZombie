from enum import Enum

import pygame

from Model.MySprite import MySprite
from constants import PIC_SUN_PATH, PIC_SUN_PATH_NUM

SUN_CENTER_X = 10
SUN_CENTER_Y = 10

class SunState(Enum):
    DIED = 0  # 时间到了的死亡状态
    STATIC = 1  # 静止状态
    MOVING = 2  # 白天产生的 竖直向下移动
    ARCMOVING = 3  # 太阳花产生的 弧线移动
    GOBAR = 4 #点击之后移动到Bar

class Sun(MySprite):

    def __init__(self, posx, posy, speed=1):
        path = "../" + PIC_SUN_PATH
        self.images = [pygame.image.load(path.format(i)) for i in range(PIC_SUN_PATH_NUM)]

        super().__init__(self.images[0])
        self.position = posx, posy

        self._state = SunState.DIED

        self.pic_index = 1
        self.left_time = 2000  # 剩余时间
        self.destination = [posx, posy]
        self.speed = speed

    def SetLineDestination(self, dest_y):
        self._state = SunState.MOVING
        self.destination[1] = dest_y

    def SetArcDestination(self, dest_x, dest_y):
        self._state = SunState.ARCMOVING
        self.destination = [dest_x, dest_y]

    def isClicked(self, mouse_click, mouse_pos):  # 检查是否被点中
        x, y = mouse_pos
        if self._state != SunState.GOBAR and mouse_click and (self.rect.x < x <= self.rect.right and
                            self.rect.y <= y <= self.rect.bottom):
            self._state = SunState.GOBAR
            return True
        return False

    def isAlive(self):
        return self._state != SunState.DIED

    def update(self):
        # super.update(self)
        if self._state == SunState.STATIC:
            if self.left_time < 0:
                self._state = SunState.DIED
            self.left_time -= 1
        elif self._state == SunState.MOVING:
            if self.Y < self.destination[1]:
                self.Y += self.speed
            else:
                self._state = SunState.STATIC
        elif self._state == SunState.ARCMOVING:
            if self.X < self.destination[0]:
                self.X += self.speed
            if self.X > self.destination[0]:
                self.X -= self.speed
            if self.Y < self.destination[1]:
                self.Y += self.speed
            if self.Y > self.destination[1]:
                self.Y -= self.speed
            if self.X == self.destination[0] and self.Y == self.destination[1]:
                self._state = SunState.STATIC
        elif self._state == SunState.GOBAR:
            if self.Y > SUN_CENTER_Y:
                self.Y -= self.speed*3
            if self.X > SUN_CENTER_X:
                self.X -= self.speed*3

            if self.X <= SUN_CENTER_X and self.Y <= SUN_CENTER_Y:
                self._state = SunState.DIED

    def draw(self, screen):
        if self._state != SunState.DIED:
            self.pic_index = self.pic_index%PIC_SUN_PATH_NUM
            screen.blit(self.images[self.pic_index], self.rect)
            self.pic_index += 1

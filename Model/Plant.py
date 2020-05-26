import pygame

from Model.Bullet import Bullet
from Model.MySprite import MySprite
from constants import *




class Plant(MySprite):


    def __init__(self, posx, posy, img):


        self.hp = 100
        self.posx = posx
        self.posy = posy
        super().__init__(img)

    def beattacked(self, down):
        self.hp -= down

    def getSprite(self):
        return self.sprite

    def update(self, *args):
        pass


class SunFlower(Plant):
    def __init__(self, posx, posy):
        self.sunFlower_image = pygame.image.load("../" + SunFlower_PATH).convert_alpha()
        super().__init__(posx, posy, self.sunFlower_image)
        self.position = posx, posy


class PeaShooter(Plant):
    def __init__(self, posx, posy):
        self.peaShooter_image = pygame.image.load("../" + PeaShooter_PATH).convert_alpha()
        super().__init__(posx, posy, self.peaShooter_image)
        self.position = posx, posy
        self.bullet = Bullet(posx+30, posy)

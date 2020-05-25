import pygame

from Model.Bullet import Bullet
from Model.MySprite import MySprite
from constants import *

sunFlower_image = pygame.image.load("../" + SunFlower_PATH).convert_alpha()
peaShooter_image = pygame.image.load("../" + PeaShooter_PATH).convert_alpha()

class Plant(MySprite):
    def __init__(self, posx, posy,img):
        self.hp = 100
        self.posx = posx
        self.posy = posy
        super.__init__(img)
        # self.image = 0

    def beattacked(self, down):
        self.hp -= down

    def getSprite(self):
        return self.sprite




class SunFlower(Plant):
    def __init__(self, posx, posy):
        super().__init__(posx, posy,sunFlower_image)
        self.position = posx, posy






class PeaShooter(Plant):
    def __init__(self, posx, posy):
        super().__init__(posx, posy,peaShooter_image)
        self.position = posx, posy
        self.bullet= Bullet(posx,posy)

    




import pygame
from Model.MySprite import MySprite
from constants import *


class Plant(MySprite):
    def __init__(self, posx, posy):
        self.hp = 100
        self.posx = posx
        self.posy = posy
        self.sprite=0
        # self.image = 0

    def beattacked(self, down):
        self.hp -= down

    def getSprite(self):
        return self.sprite




class SunFlower(Plant):
    def __init__(self, posx, posy):
        super().__init__(posx, posy)
        sunFlower_image = pygame.image.load("../" + SunFlower_PATH).convert_alpha()
        self.sprite = MySprite(sunFlower_image)
        self.sprite.position = posx, posy






class PeaShooter(Plant):
    def __init__(self, posx, posy):
        super().__init__(posx, posy)
        peaShooter_image = pygame.image.load("../" + PeaShooter_PATH).convert_alpha()
        self.sprite = MySprite(peaShooter_image)
        self.sprite.position = posx, posy
        self.power = 20

    def attack(self, zombie):
        zombie.beattacked(self.power)




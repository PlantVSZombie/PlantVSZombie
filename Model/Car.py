import pygame

from Model.MySprite import MySprite
from constants import PIC_CAR_PATH


class Car(MySprite):
    def __init__(self):
        carimg = pygame.image.load("../" + PIC_CAR_PATH).convert_alpha()
        super().__init__(carimg)


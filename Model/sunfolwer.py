import pygame
from Model.Bullet import Bullet
from Model.Zone import Zone
class SunFlower(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(SunFlower, self).__init__()
        self.images = [pygame.image.load('../resources/pics/SunFlower/SunFlower_{:d}.png'.format(i)) for i in range (17)]
        self.rect = self.images[0].get_rect()
        z=Zone()
        self.rect.left, self.rect.top =z.getGridPos(x,y)
        self.hp=150
        self.alive=True
    def setDamage(self,damage):
        self.hp-=damage
        if self.hp<0:
            self.alive=False

    def isAlive(self):
        return self.alive
import pygame
from Model.Bullet import Bullet
from Model.Zone import Zone
class PeaShooter(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(PeaShooter, self).__init__()
        self.images = [pygame.image.load('resources/pics/Peashooter/Peashooter_{:d}.png'.format(i)) for i in range (13)]
        self.rect = self.images[0].get_rect()
        self.z=Zone()
        self.rect.left, self.rect.top =self.z.getGridPos(x,y)
        self.hp=200
        self.alive=True
    def shot(self):
        return Bullet(self)
    def setDamage(self,damage):
        self.hp-=damage
        if self.hp<0:
            self.alive=False

    def getY(self):
        return self.z.getIndex(self.rect.left,self.rect.top)[1]

    def isAlive(self):
        return self.alive


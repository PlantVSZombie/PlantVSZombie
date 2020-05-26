import pygame
from Model.Bullet import Bullet
from Model.Zone import Zone
class WallNut(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(WallNut, self).__init__()
        self.images = [pygame.image.load('../resources/pics/WallNut/WallNut/WallNut_{:d}.png'.format(i)) for i in range (15)]
        self.rect = self.images[0].get_rect()
        z=Zone()
        self.rect.left, self.rect.top =z.getGridPos(x,y)
        self.hp=600
        self.alive=True
    def setDamage(self,damage):
        self.hp-=damage
        if self.hp<0:
            self.alive=False

    def isAlive(self):
        return self.alive
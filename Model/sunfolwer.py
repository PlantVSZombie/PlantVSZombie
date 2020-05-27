import pygame
from Model.Bullet import Bullet
from Model.Sun import Sun
from Model.Zone import Zone


class SunFlower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(SunFlower, self).__init__()
        self.images = [pygame.image.load('../resources/pics/SunFlower/SunFlower_{:d}.png'.format(i)) for i in range(17)]
        self.golden = [pygame.image.load('../resources/pics/GoldenSunFlower/GoldenSunFlower_{:d}.png'.format(i)) for i in range(14,18)]
        self.rect = self.images[0].get_rect()
        z = Zone()
        self.rect.left, self.rect.top = z.getGridPos(x, y)
        self.hp = 150
        self.times = 0
        self.alive = True

    def setDamage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.alive = False

    def produce(self):
        sun = Sun(self.rect.left - 10, self.rect.top - 40)
        sun.SetArcDestination(self.rect.left + 20, self.rect.top + 50)
        return sun

    def isAlive(self):
        return self.alive

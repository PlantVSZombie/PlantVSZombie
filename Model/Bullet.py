import pygame
from constants import *
from Model.MySprite import MySprite


class Bullet(MySprite):
    def __init__(self, posx, posy):
        self.normalBullet_img = pygame.image.load("../" + BulletNormal_PATH).convert_alpha()
        self.explodeBullet_img = pygame.image.load("../" + BulletExplode_PATH).convert_alpha()

        self.posx = posx + 1
        self.posy = posy
        self.power = 20
        self.beginx = posx
        self.state = "normal"

        super().__init__(self.normalBullet_img)
        self.position = posx, posy

    def attack(self, zombie):
        zombie.setDamage(self.power)

    def update(self, *args):
        if self.state == "normal":
            super().__init__(self.normalBullet_img)
            self.position = self.posx, self.posy
            self.posx += 8
        else:
            super().__init__(self.explodeBullet_img)
            self.position = self.posx, self.posy
            self.posx = self.beginx
            self.state = "normal"

    def boom(self):
        self.state = "explode"

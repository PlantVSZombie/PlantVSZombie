import pygame
from constants import *
from Model.MySprite import MySprite


class Bullet(pygame.sprite.Sprite):
    def __init__(self, plant):
        super(Bullet,self)
        self.normalBullet_img = pygame.image.load("../" + BulletNormal_PATH).convert_alpha()
        # self.explodeBullet_img = pygame.image.load("../" + BulletExplode_PATH).convert_alpha()

        self.rect=self.normalBullet_img.get_rect()
        self.rect.left=plant.rect.left+35
        self.rect.top=plant.rect.top
        self.power = 20
        self.state = "normal"



    def attack(self, enemyList):
        for enemy in enemyList:
            if pygame.sprite.collide_circle_ratio(0.5)(enemy,self):
                self.state="boom"
                self.normalBullet_img = pygame.image.load("../" + BulletExplode_PATH).convert_alpha()
                enemy.setDamage(self.power)



    def update(self):

        if self.rect.left<1000:
            if self.state == "normal":
                self.rect.left+=8
        else:
            self.state="out"

    def boom(self):
        self.state = "explode"

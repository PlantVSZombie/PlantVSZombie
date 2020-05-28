import pygame
from Model.Zone import Zone
import random


class Zombie(pygame.sprite.Sprite):
    def __init__(self,x):
        self.images = [pygame.image.load('resources/pics/Zombies/NormalZombie/Zombie/Zombie_{:d}.png'.format(i)) for i in
                       range(20)]
        self.rect = self.images[0].get_rect()
        self.z=Zone()
        self.rect.left=self.z.getGridPos(x,random.randint(0,1))[0]
        self.rect.top =self.z.getGridPos(x,random.randint(0,4))[1]-60
        self.speed=2
        self.hp=100
        self.is_alive=True
        self.is_attack=False
        self.power=15

    def move(self):
        #if self.rect.left<self.z.MAP_OFFSET_X-200:
        #     self.is_alive=False
        if not self.is_attack:
            self.rect.left-=self.speed
        if self.hp<40:
            self.images = [
                pygame.image.load('resources/pics/Zombies/NormalZombie/ZombieLostHead/ZombieLostHead_{:d}.png'.format(i))
                for i in range(20)]
        else:
            self.images = [pygame.image.load('resources/pics/Zombies/NormalZombie/Zombie/Zombie_{:d}.png'.format(i))
                           for i in
                           range(20)]

    def setDamage(self,damage):
        self.hp-=damage

        if self.hp<0:
            self.is_alive=False

    def getY(self):
        return self.z.getIndex(self.rect.left,self.rect.top+60)[1]

    def attack(self,enemyList):
        for enemy in enemyList:
            # enemy.rect.left,enemy.rect.top=enemy.rect
            if pygame.sprite.collide_circle_ratio(0.5)(enemy,self):
                self.is_attack=True
                enemy.setDamage(self.power)
                if enemy.isAlive()==False:
                    self.is_attack=False
                if self.hp<40:
                    self.images = [pygame.image.load('resources/pics/Zombies/NormalZombie/ZombieLostHeadAttack/ZombieLostHeadAttack_{:d}.png'.format(i)) for i in range(20)]
                else:
                    self.images = [pygame.image.load('resources/pics/Zombies/NormalZombie/ZombieAttack/ZombieAttack_{:d}.png'.format(i))for i in range(20)]







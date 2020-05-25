import pygame


class Zombie():
    def __init__(self):
        self.images = [pygame.image.load('../resources/pics/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie_{:d}.png'.format(i)) for i in
                       range(14)]
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = 1200, 250
        self.speed=5

    def move(self):
        self.rect.left-=self.speed





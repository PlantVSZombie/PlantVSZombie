import pygame
class PeaShooter:
    def __init__(self):
        self.images = [pygame.image.load('../resources/pics/Peashooter/Peashooter_{:d}.png'.format(i)) for i in range (13)]
        self.rect = self.images[0].get_rect()
        self.rect.left,self.rect.top=400,300

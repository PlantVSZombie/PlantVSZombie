from unittest import TestCase
import datetime
import pygame
from Model import Menubar

class TestCard(TestCase):
    def test_something(self):
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("测试卡片")
        map =pygame.image.load('../resources/pics/items/Background_0.jpg')
        screen.blit(map,(0,0))
        menu=Menubar.Menubar(10,10,[0,1],100)
        menu.draw(screen)

        while True:
            x, y = pygame.mouse.get_pos()
            item=menu.checkCardChosen((x,y))
            if item!=None:
                item.setShowImage(menu.sun_value,pygame.time.get_ticks())
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

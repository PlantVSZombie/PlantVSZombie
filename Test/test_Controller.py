from unittest import TestCase

import pygame

from Controller.Controller import Controller


class TestController(TestCase):
    def test_initiate(self):
        screen_size = (1200, 600)
        screen = pygame.display.set_mode(screen_size)
        Controller(screen)

    def test_deal_card_selected(self):
        self.fail()

    def test_deal_sow(self):
        self.fail()

    def test_sow_plant(self):
        self.fail()

    def test_update_plant_list(self):
        self.fail()

    def test_update_zombie_list(self):
        self.fail()

    def test_update_bullet_list(self):
        self.fail()

from unittest import TestCase
import constants as c
from Model.tool import load_image_frames


class TestLoad_image_frames(TestCase):
    def test_load_image_frames(self):
        load_image_frames('resources/pics/Zombies/BucketheadZombie/BucketheadZombie','BucketheadZombie_0.png',c.WHITE,accept=('.png', '.jpg', '.bmp', '.gif'))

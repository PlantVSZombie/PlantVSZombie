import pygame as pg


class Button:
    def __init__(self, x, y, pic_path, pic_path2=None,action=None):
        self.rect = None
        self.image = None
        self.x = x
        self.y = y
        self.load_img(pic_path)

        self.pic=pic_path
        self.pic2=pic_path2
        self.enable = True
        self.action = action

    def load_img(self,pic_path):
        frame = pg.image.load(pic_path).convert_alpha()
        self.rect = frame.get_rect()
        self.image = pg.Surface([self.rect.width, self.rect.height])
        self.image.blit(frame, (0, 0), self.rect)
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.set_colorkey((255,255,255))

    def isClicked(self, mouse_click, mouse_pos):  # 检查是否被点中
        x, y = mouse_pos
        if self.enable and mouse_click and (self.rect.x < x <= self.rect.right and
                                            self.rect.y <= y <= self.rect.bottom):
            if self.pic2 is not None:
                self.load_img(self.pic2)
            if self.action is not None:
                self.action()
            return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)


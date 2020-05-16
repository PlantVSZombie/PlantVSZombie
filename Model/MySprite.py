import pygame



class MySprite(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        #图片可以使用pygame.image.load("filename").convert_alpha()
        self.image = image
        #rect 最好使用 Rect(x,y,width,height)来创建
        self.rect = image.get_rect()
    #X 属性
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    X = property(_getx,_setx)

    #Y 属性
    def _gety(self): return self.rect.y
    def _sety(self,value): self.rect.y = value
    Y = property(_gety,_sety)

    #position 属性
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)
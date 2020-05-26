import random
import pygame as pg
import constants as c
BLOCK_WIDTH=80
BLOCK_HEIGHT=100
LEFTTOP=(256,74)

plant_name_list = ['../resources/pics/items/SunFlower_0.png', '../resources/pics/items/card_peashooter.png']

class GrassBlock():
    '''用草坪框左上角坐标'''
    def __init__(self,x,y):
        self.width=BLOCK_WIDTH
        self.height=BLOCK_HEIGHT
        self.x=x
        self.y=y
        self.centre=(int(x+self.width/2),int(y+self.height/2))#设置方块中心，到时候plant和zombie都种在这
        self.occupied=False #是否被占据
    def setOccupied(self,state):
        self.occupied=state
    def getOccupied(self):
        return self.occupied
    def getCentre(self):
        return self.centre
    '''检查鼠标是否在该草坪块的上方'''
    def checkAbove(self,mouse_pos):#检查鼠标是不是在上面
        x,y=mouse_pos
        if (x>self.x and x<=self.x+self.width and
        y>=self.y and y<=self.y+self.height):
            return True
        return False
    '''检查鼠标否在该块进行点击'''
    def checkSelected(self,mouse_pos,mos_click):
        if mos_click and self.checkAbove(mouse_pos):
            print("be clicked")
            return True
        return False
class Map():
    def __init__(self,surface):
        self.loadFrame(surface)
        self.setBlock()
    def loadFrame(self,surface):#加载背景图片
        self.map = pg.image.load('../resources/pics/items/Background_0.jpg')
        surface.blit(self.map, (0, 0))
    def setBlock(self):
        x,y=LEFTTOP
        self.block_list=[]
        for i in range(9):
            for j in range(5):
                self.block_list.append(GrassBlock(x+i*BLOCK_WIDTH,y+j*BLOCK_HEIGHT))
    '''检查'''
    def checkAbove(self,mouse_pos):
        for block in self.block_list:
            if block.checkAbove(mouse_pos):
                return block
        return None
    def draw(self,surface):
        surface.blit(self.map,(0,0))

import random
import pygame as pg
import constants as c

PANEL_Y_START = 87
PANEL_X_START = 22
PANEL_Y_INTERNAL = 74
PANEL_X_INTERNAL = 53
CARD_LIST_NUM = 8

card_name_list = ['../resources/pics/items/card_sunflower.png', '../resources/pics/items/card_peashooter.png']
plant_sun_list = [50, 100]
plant_frozen_time_list = [7500, 7500]
all_card_list = [0, 1]


class Card():
    def __init__(self,x,y,name_index):
        self.loadFrame(card_name_list[name_index])
        self.rect.x=x#(x,y)为左上角坐标
        self.rect.y=y
        self.name_index = name_index #名字索引
        self.sun_cost = plant_sun_list[name_index]
        self.frozen_time = plant_frozen_time_list[name_index]
        self.frozen_timer=-self.frozen_time#被冷冻的时间点
        self.chosen=False
    def getChosen(self):
        return self.chosen
    '''加载卡片上的图片'''
    def loadFrame(self,name):
        frame=pg.image.load(name).convert_alpha()
        self.rect = frame.get_rect()
        #这tm的还要转换一下图片格式
        self.root_image=frame
        self.temp_image=self.root_image
    '''检查该卡片是否被选中'''
    def checkChosen(self,mouse_pos):#检查是否被选中
        x,y=mouse_pos
        if (x>self.rect.x and x<=self.rect.right and
        y>=self.rect.y and y<=self.rect.bottom):
            return True
        return False
    def setFrozenTimer(self,current_time):
        self.frozen_timer=current_time
    '''设置成被选中'''
    def setChosen(self):
        self.temp_image.set_alpha(128)
        self.chosen=True
    '''设置成未选中'''
    def setUnchosen(self):
        self.temp_image.set_alpha(255)
        self.chosen=False
    '''正常时或者当太阳不足或者冷却时间不足时，展示图片'''
    def setShowImage(self,sun_value,current_time):
        tem_time=current_time-self.frozen_timer
        if tem_time<self.frozen_time:
            image=pg.Surface([self.rect.w,self.rect.h])#建一张新空白图片
            frozen_image = self.root_image.copy()
            frozen_image.set_alpha(128)
            frozen_hight=(self.frozen_time-tem_time)/self.frozen_time*self.rect.h
            image.blit(frozen_image,(0,0),(0,0,self.rect.w,frozen_hight))
            image.blit(self.root_image,(0,frozen_hight),(0,frozen_hight,self.rect.w,self.rect.h-frozen_hight))
        elif self.sun_cost<sun_value:
            image=self.root_image.copy()
            image.set_alpha(200)
        else:
            image = self.root_image.copy()
        return image

    def update(self,sun_value,current_time):
        #得慢慢更新，要不显示不出回复效果
        self.temp_image=self.setShowImage(sun_value,current_time)
    def draw(self,surface):
        surface.blit(self.temp_image,self.rect)
class Menubar():
    def __init__(self,x,y,card_list,sun_value):
        self.loadFrame('../resources/pics/items/ChooserBackground.png')
        self.rect.x=x
        self.rect.y=y
        self.sun_value=sun_value
        self.card_offset_x=32
        self.setCards(card_list)#card_list是index值
    def loadFrame(self,name):
        self.image=pg.image.load(name).convert_alpha()
        self.rect=self.image.get_rect()
    '''增减阳光数值'''
    def incSunValue(self,value):
        self.sun_value+=value
    def decSunValue(self,value):
        self.sun_value-=value
    '''获得阳光数值图片'''
    def getSunValueImage(self,sun_value):
        font = pg.font.SysFont(None, 22)
        width = 32
        msg_image = font.render(str(sun_value), True, c.NAVYBLUE, c.LIGHTYELLOW)
        msg_rect = msg_image.get_rect()
        msg_w = msg_rect.width

        image = pg.Surface([width, 17])
        x = width - msg_w

        image.fill(c.LIGHTYELLOW)
        image.blit(msg_image, (x, 0), (0, 0, msg_rect.w, msg_rect.h))
        image.set_colorkey(c.BLACK)
        return image
    '''将阳光数值图片贴到相应位置'''
    def drawSunValue(self):
        self.value_image=self.getSunValueImage(self.sun_value)
        self.value_rect=self.value_image.get_rect()
        self.value_rect.x = 21
        self.value_rect.y = self.rect.bottom - 21
        self.image.blit(self.value_image, self.value_rect)
    '''检查bar内卡片是否被点击，并返回相应卡片信息'''
    def checkCardChosen(self,mouse_pos):
        for card in self.card_list:
            if card.checkChosen(mouse_pos):
                return card
        return None
    '''设置卡片的冷冻时间点'''
    def setCardFrozenTimer(self,current_time,card):
        for i in self.card_list:
            if i.name_index==card.name_index:
                card.setFrozenTimer(current_time)
                break
    '''设置卡片'''
    def setCards(self,card_list):
        self.card_list=[]
        x=self.card_offset_x
        y=8
        for index in card_list:
            x += 55
            self.card_list.append(Card(x, y, index))
    '''绘画'''
    def draw(self, surface):
        self.drawSunValue()
        surface.blit(self.image, self.rect)
        for card in self.card_list:
            card.draw(surface)


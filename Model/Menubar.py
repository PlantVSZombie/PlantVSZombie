import random
import pygame as pg
import constants as c

PANEL_Y_START = 87
PANEL_X_START = 22
PANEL_Y_INTERNAL = 74
PANEL_X_INTERNAL = 53
CARD_LIST_NUM = 8

card_name_list = ['../resources/pics/cards/card_sunflower.png', '../resources/pics/cards/card_peashooter.png',
                  '../resources/pics/cards/card_wallnut.png']
plant_sun_list = [50, 100,50]
plant_frozen_time_list = [7500, 7500,30000]
all_card_list = [0, 1,2]

'''Card'''
class Card():
    def __init__(self,x,y,name_index):
        self.loadFrame(card_name_list[name_index])
        self.rect.x=x#(x,y)为左上角坐标
        self.rect.y=y
        self.name_index = name_index #名字索引
        self.sun_cost = plant_sun_list[name_index]
        self.frozen_time = plant_frozen_time_list[name_index]
        self.frozen_timer=-self.frozen_time#被冷冻的时间点
        self.befrozen=False

    '''获取name_index，以此来跟plant产生联系'''
    def getIndex(self):
        return self.name_index

    '''加载卡片上的图片'''
    def loadFrame(self,name):
        frame=pg.image.load(name).convert_alpha()
        self.rect = frame.get_rect()
        image = pg.Surface([self.rect.width, self.rect.height])
        image.blit(frame, (0, 0), self.rect)
        image=pg.transform.scale(image,(int(self.rect.width*0.78),int(self.rect.height*0.78)))#缩小尺寸
        self.rect.w=int(self.rect.width * 0.78)
        self.rect.h = int(self.rect.height * 0.78)
        self.root_image=image
        self.temp_image=self.root_image
    '''检查该卡片是否被选中'''
    def checkChosen(self,mouse_click,mouse_pos):#检查是否被选中
        x,y=mouse_pos
        if mouse_click and (x>self.rect.x and x<=self.rect.right and
        y>=self.rect.y and y<=self.rect.bottom):
            return True
        return False
    def setFrozenTimer(self,current_time):
        self.frozen_timer=current_time
        self.befrozen=True
    '''设置成被选中'''
    def setChosen(self):
        self.temp_image.set_alpha(128)
    '''设置成未选中'''
    def setUnchosen(self):
        self.temp_image.set_alpha(255)
    def getSunCost(self):
        return self.sun_cost
    '''返回是否处于冷冻状态'''
    def getIfFrozen(self):
        return self.befrozen
    '''正常时或者当太阳不足或者冷却时间不足时，展示图片'''
    def setShowImage(self,sun_value,current_time):
        tem_time=current_time-self.frozen_timer
        if tem_time<self.frozen_time:#冷冻中
            image=pg.Surface([self.rect.w,self.rect.h])#建一张新空白图片
            frozen_image = self.root_image.copy()
            frozen_image.set_alpha(128)
            frozen_hight=(self.frozen_time-tem_time)/self.frozen_time*self.rect.h
            image.blit(frozen_image,(0,0),(0,0,self.rect.w,frozen_hight))
            image.blit(self.root_image,(0,frozen_hight),(0,frozen_hight,self.rect.w,self.rect.h-frozen_hight))
        else:
            self.befrozen=False #冷冻解除
            if self.sun_cost>sun_value:#太阳不足
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
        self.card_offset_x=24
        self.card_offset_y = 8
        self.setCards(card_list)#card_list是index值
    def loadFrame(self,name):
        frame = pg.image.load(name).convert_alpha()
        self.rect = frame.get_rect()
        self.image = pg.Surface([self.rect.width, self.rect.height])
        self.image.blit(frame, (0, 0), self.rect)
    '''增减阳光数值'''
    def incSunValue(self,value):
        self.sun_value+=value
    def decSunValue(self,value):
        self.sun_value-=value
    def getSunValue(self):
        return self.sun_value
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
        self.value_rect.x = 20
        self.value_rect.y = self.rect.y+self.rect.h - 31
        self.image.blit(self.value_image, self.value_rect)
    '''检查bar内卡片是否被点击，并返回相应卡片信息'''
    def checkCardChosen(self,mouse_click,mouse_pos):
        for card in self.card_list:
            if card.checkChosen(mouse_click,mouse_pos):
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
        y=self.card_offset_y
        for index in card_list:
            x += 55
            self.card_list.append(Card(x, y, index))
    '''对自己的卡片进行更新'''
    def update(self,sun_value,current_time):
        self.current_time=current_time
        for card in self.card_list:
            card.update(sun_value,self.current_time)
    '''绘画'''
    def draw(self, surface):
        self.drawSunValue()
        surface.blit(self.image, self.rect)
        for card in self.card_list:
            card.draw(self.image)
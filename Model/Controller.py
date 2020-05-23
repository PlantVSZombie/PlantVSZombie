import pygame
from Model.MySprite import MySprite
from constants import *
from Model.Plant import *
from pygame.locals import *
import sys, time

'''判断卡片是否被选择并且做出相应动作
    传参：鼠标位置，鼠标点击，菜单实例
'''
def dealCardSelected(mos_pos,mos_click,menu):
    item = menu.checkCardChosen(mos_click, mos_pos)
    if item != None:
        if item.getIfFrozen():#如果冷冻状态,不响应
            return
        menu_sun=menu.getSunValue()
        card_sun=item.getSunCost()
        if menu_sun>=card_sun:#如果阳光够可选，减掉相应数值
            menu.setCardFrozenTimer(pygame.time.get_ticks(),item)
            menu.decSunValue(card_sun)
        else:#如果阳光不够不可选，不响应
            return
    return

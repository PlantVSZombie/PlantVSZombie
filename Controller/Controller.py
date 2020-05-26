import pygame
from Model.Plant import *
from Model import Map
from Model import Menubar
from Model.Sun import Sun

SCREEN_WIDTH=1200
SCREEN_HEIGHT=600

class Controller():
    def __init__(self):
        self.cursor_changed=False#当前鼠标是否被替换
        self.plant_index=0#当前替换鼠标的植物索引
        self.initiate()
    '''负责启动整个游戏界面'''
    def initiate(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("测试卡片")
        self.map = Map.Map(self.screen)
        self.menu = Menubar.Menubar(10, 10, [0, 1,2], 200)
        self.menu.draw(self.screen)
        temp_item=None

        while True:
            self.map.draw(self.screen)
            self.menu.draw(self.screen)
            mos_pos = pygame.mouse.get_pos()
            (mos_click, _, _) = pygame.mouse.get_pressed()
            item=self.dealCardSelected(mos_pos, mos_click, self.menu)  # 调用Controller类的管理函数
            if item != None:
                temp_item=item
            '''下面的内容是将鼠标替换成对应植物图片，因为放在函数里实现不了，就把它放在主循环当中了'''
            if self.cursor_changed==True: #如果鼠标被标记为已更改
                mouse_cursor = pygame.image.load(Map.plant_name_list[self.plant_index]).convert_alpha()
                pygame.mouse.set_visible(False)
                x, y = mos_pos
                x -= mouse_cursor.get_width() / 2
                y -= mouse_cursor.get_height() / 2
                # 用其他图形代替鼠标
                self.screen.blit(mouse_cursor, (x, y))
            elif temp_item!=None:
                pygame.mouse.set_visible(True)
            if temp_item!=None:
                self.dealSow(mos_click,temp_item)


            self.menu.update(self.menu.sun_value, pygame.time.get_ticks())
            self.menu.draw(self.screen)


            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    '''判断卡片是否被选择并且做出相应动作
        传参：鼠标位置，鼠标点击，菜单实例
    '''
    def dealCardSelected(self,mos_pos, mos_click, menu):
        item = menu.checkCardChosen(mos_click, mos_pos)#item代表被点击的Card
        if item != None:
            if item.getIfFrozen():  # 如果冷冻状态,不响应
                return None
            menu_sun = menu.getSunValue()
            card_sun = item.getSunCost()
            if menu_sun >= card_sun:  # 如果阳光够,可选
                item.setChosen()
                self.cursor_changed=True
                self.plant_index=item.getIndex()
                item.setChosen()
                return item
            else:  # 如果阳光不够不可选，不响应
                return None
        return None
    '''选择植物将要种植时的处理'''
    def dealSow(self,click,item):
        # 监听是否再次点击，如果再点击就要种植物了
        if click and self.cursor_changed == True:
            x, y = pygame.mouse.get_pos()
            block = self.map.checkAbove((x, y))  # block代表被点击的草坪块
            if block != None and block.getOccupied()==False:
                block.setOccupied(True)  # 设置成该块被占据，以后就不能再种了
                centre_pos = block.getCentre()##需要改成行列
                row=int(centre_pos[1]/Map.BLOCK_HEIGHT)
                col=int((centre_pos[0]-Map.LEFTTOP[0])/Map.BLOCK_WIDTH)
                col=max(col,0)
                self.sowPlant(col,row, self.plant_index)  # 种植物
                self.cursor_changed = False  # 不替换
                self.menu.setCardFrozenTimer(pygame.time.get_ticks(), item)
                self.menu.decSunValue(item.getSunCost())
    ''' 播种植物，在内部需要将mos_pos修改成几行几列，给Plant用;
        index=0则种向日葵，index=1则种豌豆射手。
    '''
    def sowPlant(self,col,row,index):

        return 0
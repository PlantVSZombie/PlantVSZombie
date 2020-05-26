import pygame
from Model.MySprite import MySprite
from Model.Sun import Sun
from constants import *
from Model.PeaShooter import PeaShooter
from Model.sunfolwer import SunFlower
from Model.wallnut import WallNut
from Model.Car import Car
from Model import Map
from Model import Menubar
import random
from pygame.locals import *
import sys, time

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

sun_max = 10
sun_index = 0


class Controller():
    def __init__(self):
        self.cursor_changed = False  # 当前鼠标是否被替换
        self.plant_index = 0  # 当前替换鼠标的植物索引
        self.sun_max = 20
        self.sun_index = 0

        self.peaShooterList = []
        self.sunFlowerList = []
        self.wallnutList = []
        self.zombieList = []
        self.bulletList = []
        self.carList = []
        self.sunList = []
        self.has_zombie = [0, 0, 0, 0, 0]
        self.display_index = 0  # 当前要显示的图片
        self.initiate()

    '''负责启动整个游戏界面'''

    def initiate(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("测试卡片")
        self.map = Map.Map(self.screen)
        self.menu = Menubar.Menubar(10, 10, [0, 1, 2], 200)
        self.menu.draw(self.screen)
        temp_item = None
        block = pygame.time.Clock()
        for i in range(5):
            car = Car.CreateCarAtRow(i)  # 第i行的车 对不齐是getGridPos函数可能有点问题
            self.carList.append(car)
        while True:
            block.tick(15)
            self.map.draw(self.screen)
            self.menu.draw(self.screen)
            mos_pos = pygame.mouse.get_pos()
            (mos_click, _, _) = pygame.mouse.get_pressed()
            item = self.dealCardSelected(mos_pos, mos_click, self.menu)  # 调用Controller类的管理函数
            if item != None:
                temp_item = item
            '''下面的内容是将鼠标替换成对应植物图片，因为放在函数里实现不了，就把它放在主循环当中了'''
            if self.cursor_changed == True:  # 如果鼠标被标记为已更改
                mouse_cursor = pygame.image.load(Map.plant_name_list[self.plant_index]).convert_alpha()
                pygame.mouse.set_visible(False)
                x, y = mos_pos
                x -= mouse_cursor.get_width() / 2
                y -= mouse_cursor.get_height() / 2
                # 用其他图形代替鼠标
                self.screen.blit(mouse_cursor, (x, y))
            elif temp_item != None:
                pygame.mouse.set_visible(True)
            if temp_item != None:
                self.dealSow(mos_click, temp_item)

            self.menu.update(self.menu.sun_value, pygame.time.get_ticks())
            # 对plantList更新并绘制
            self.updatePeaShooterList()
            self.updateSunFlowerList()
            self.updateWallnutList()
            # 对zombieList更新并绘制
            self.updateZombieList()
            # 对bulletList更新并绘制
            self.updateBulletList()
            # 对carList更新并绘制
            self.updateCarList()
            # 对sunList更新并绘制
            self.updateSunList()

            self.menu.draw(self.screen)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.display_index += 1

    '''判断卡片是否被选择并且做出相应动作
        传参：鼠标位置，鼠标点击，菜单实例
    '''

    def dealCardSelected(self, mos_pos, mos_click, menu):
        item = menu.checkCardChosen(mos_click, mos_pos)  # item代表被点击的Card
        if item != None:
            if item.getIfFrozen():  # 如果冷冻状态,不响应
                return None
            menu_sun = menu.getSunValue()
            card_sun = item.getSunCost()
            if menu_sun >= card_sun:  # 如果阳光够,可选
                item.setChosen()
                self.cursor_changed = True
                self.plant_index = item.getIndex()
                item.setChosen()
                return item
            else:  # 如果阳光不够不可选，不响应
                return None
        return None

    '''选择植物将要种植时的处理'''

    def dealSow(self, click, item):
        # 监听是否再次点击，如果再点击就要种植物了
        if click and self.cursor_changed == True:
            x, y = pygame.mouse.get_pos()
            block = self.map.checkAbove((x, y))  # block代表被点击的草坪块
            if block != None and block.getOccupied() == False:
                block.setOccupied(True)  # 设置成该块被占据，以后就不能再种了
                centre_pos = block.getCentre()  ##需要改成行列
                row = int(centre_pos[1] / Map.BLOCK_HEIGHT)
                col = int((centre_pos[0] - Map.LEFTTOP[0]) / Map.BLOCK_WIDTH)
                col = max(col, 0)
                self.sowPlant(col, row, self.plant_index)  # 种植物
                self.cursor_changed = False  # 不替换
                self.menu.setCardFrozenTimer(pygame.time.get_ticks(), item)
                self.menu.decSunValue(item.getSunCost())

    ''' 播种植物，在内部需要将mos_pos修改成几行几列，给Plant用;
        index=0则种向日葵，index=1则种豌豆射手。
    '''

    def sowPlant(self, col, row, index):
        if index == 0:
            self.sunFlowerList.append(SunFlower(col, row))
        if index == 1:
            self.peaShooterList.append(PeaShooter(col, row))
        if index == 2:
            self.wallnutList.append(WallNut(col, row))

    def updatePeaShooterList(self):
        for plant in self.peaShooterList:
            if self.display_index % 20 == 1 and self.has_zombie[plant.getY()] > 0:
                bullet = plant.shot()
                self.bulletList.append(bullet)
            self.screen.blit(plant.images[self.display_index % 13], plant.rect)

            if plant.alive == False:
                self.plantList.remove(plant)

    def updateSunFlowerList(self):
        for sunflower in self.sunFlowerList:
            if self.display_index % 18 == 17:
                if sunflower.times == 5:
                    sun = sunflower.produce()  # 要添加向日葵变金色，可在类里
                    self.sunList.append(sun)
                    sunflower.times = 0
                else:
                    sunflower.times += 1
            self.screen.blit(sunflower.images[self.display_index % 17], sunflower.rect)
            if sunflower.isAlive() == False:
                self.sunFlowerList.remove(sunflower)

    def updateWallnutList(self):
        for wallnut in self.wallnutList:
            self.screen.blit(wallnut.images[self.display_index % 15], wallnut.rect)
            if wallnut.isAlive() == False:
                self.wallnutList.remove(wallnut)

    def updateZombieList(self):

        for zombie in self.zombieList:
            self.screen.blit(zombie.images[self.display_index % 20], zombie.rect)
            zombie.move()
            zombie.attack(self.peaShooterList)
            zombie.attack(self.wallnutList)
            zombie.attack(self.sunflowerList)
            if zombie.is_alive == False:
                self.zombieList.remove(zombie)
                self.has_zombie[zombie.getY()] -= 1

    def updateBulletList(self):
        for bullet in self.bulletList:
            if bullet.state != "out":
                if bullet.state == "boom":
                    self.bulletList.remove(bullet)
                self.screen.blit(bullet.normalBullet_img, bullet.rect)
                bullet.update()
                bullet.attack(self.zombieList)
            else:

                self.bulletList.remove(bullet)

    def updateCarList(self):
        for car in self.carList:
            car.check(self.zombieList)  # 检测是否有碰撞
            car.update()  # 更新状态
            car.draw(self.screen)  # 绘图
            if car.isRUN_OUT_SCREEN():  # 小车跑出去了
                self.carList.remove(car)

    def updateSunList(self):
        if self.sun_index >= self.sun_max:
            sun = Sun(random.randint(200, 800), 0, 5)  # 初始X，Y坐标
            sun.SetLineDestination(random.randint(50, 500))  # 直线下降 参数：目标Y坐标 白天自动生成的
            self.sunList.append(sun)
            self.sun_index = 0
        else:
            self.sun_index += 1
        x, y = pygame.mouse.get_pos()
        mouse_click, _, _ = pygame.mouse.get_pressed()
        for sun in self.sunList:
            sun.update()  # 更新状态
            if sun.isAlive():
                sun.draw(self.screen)
                if sun.isClicked(mouse_click, (x, y)):
                    self.menu.incSunValue(25)
                    print("阳光+25")
            else:
                self.sunList.remove(sun)

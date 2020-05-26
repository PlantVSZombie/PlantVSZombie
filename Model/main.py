import random
import sys

import pygame

from Model.Car import Car
from Model.PeaShooter import PeaShooter
from Model.Sun import Sun
from Model.Zombie import Zombie
from Model.Zone import Zone
from Model.sunfolwer import SunFlower
from Model.wallnut import WallNut

if __name__ == '__main__':
    zone=Zone()

    has_zombie=[0,0,0,0,0]

    zombieList=[]
    zombie = Zombie(7)
    zombieList.append(zombie)
    has_zombie[zombie.getY()]+=1
    zombie1 = Zombie(8)
    zombieList.append(zombie1)
    has_zombie[zombie1.getY()] += 1
    zombie2 = Zombie(9)
    zombieList.append(zombie2)
    has_zombie[zombie2.getY()] += 1

    wallnutList=[]
    sunflowerList=[]
    peaList=[]
    peashooter=PeaShooter(0,0)
    wallnut=WallNut(6,1)
    sunflower=SunFlower(5,1)
    peaList.append(peashooter)
    sunflowerList.append(sunflower)
    wallnutList.append(wallnut)
    block=pygame.time.Clock()
    bulletList=[]
    pygame.init()
    screen_size=(1200,600)
    screen=pygame.display.set_mode(screen_size)
    pygame.display.set_caption('郑祺琛的house')
    img_background_path='../resources/pics/items/Background_0.jpg'
    backGroup=pygame.image.load(img_background_path).convert()
    index=0

    cars = []
    for i in range(5):
        car = Car.CreateCarAtRow(i)  # 第i行的车
        cars.append(car)

    suns=[]
    sun_index=0
    sun_max=20 #控制多久产生一个太阳

    while True:

        block.tick(15)
        # #绘制背景



        screen.blit(backGroup,(0,0))
        for sunflower in sunflowerList:
            screen.blit(sunflower.images[index % 17], sunflower.rect)
            if sunflower.isAlive()==False:
                sunflowerList.remove(sunflower)
        for wallnut in wallnutList:
            screen.blit(wallnut.images[index % 15], wallnut.rect)
            if wallnut.isAlive()==False:
                wallnutList.remove(wallnut)


        for pea in peaList:
            if index % 20 == 1 and has_zombie[pea.getY()]>0:
                bullet =pea.shot()
                bulletList.append(bullet)
            screen.blit(pea.images[index%13],pea.rect)

            if pea.alive==False:
                peaList.remove(pea)
        for zombie in zombieList:
            screen.blit(zombie.images[index % 20], zombie.rect)
            zombie.move()
            zombie.attack(peaList)
            zombie.attack(wallnutList)
            zombie.attack(sunflowerList)
            if zombie.is_alive==False:
                zombieList.remove(zombie)
                has_zombie[zombie.getY()]-=1

        for bullet in bulletList:
            if bullet.state!="out":
                if bullet.state == "boom":
                    bulletList.remove(bullet)
                screen.blit(bullet.normalBullet_img, bullet.rect)
                bullet.update()
                bullet.attack(zombieList)
            else:

                bulletList.remove(bullet)


        for car in cars:
            car.check(zombieList)
            car.update() #更新状态
            car.draw(screen)
            if car.isRUN_OUT_SCREEN():
                cars.remove(car)

        if sun_index>=sun_max:
            sun = Sun(random.randint(200,800), 0,5) #初始X，Y坐标
            sun.SetLineDestination(random.randint(50,500))  # 直线下降 参数：目标Y坐标 白天自动生成的
            suns.append(sun)
            sun_index=0
        else:
            sun_index+=1

        x, y = pygame.mouse.get_pos()
        mouse_click, _, _ = pygame.mouse.get_pressed()

        for sun in suns:
            sun.update() #更新状态
            if sun.isAlive():
                sun.draw(screen)
                if sun.isClicked(mouse_click, (x, y)):
                    print("阳光+10")
            else:
                suns.remove(sun)

        pygame.display.update()
        index+=1
        #实现右上角关闭
        for event in pygame.event.get():
            # x,y=pygame.mouse.get_pos()
            # if event.type==pygame.MOUSEMOTION:
            #     print(zone.getIndex(x,y))


            if event.type==pygame.QUIT:
                sys.exit()





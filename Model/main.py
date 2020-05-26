import random
import sys

import pygame

from Model.Car import Car
from Model.PeaShooter import PeaShooter
from Model.Sun import Sun
from Model.Zombie import Zombie
from Model.Zone import Zone

if __name__ == '__main__':
    zone=Zone()

    zombieList=[]
    zombie = Zombie(7)
    zombieList.append(zombie)
    zombie1 = Zombie(8)
    zombieList.append(zombie1)
    zombie2 = Zombie(9)
    zombieList.append(zombie2)


    plantList=[]
    peashooter=PeaShooter(2,0)
    plantList.append(peashooter)
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
        for plant in plantList:
            if index % 20 == 1:
                bullet =plant.shot()
                bulletList.append(bullet)
            screen.blit(plant.images[index%13],plant.rect)

            if plant.alive==False:
                plantList.remove(plant)
        for zombie in zombieList:
            screen.blit(zombie.images[index % 20], zombie.rect)
            zombie.move()
            zombie.attack(plantList)
            if zombie.is_alive==False:
                zombieList.remove(zombie)

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
            sun.SetLineDestination(200)  # 直线下降 参数：目标Y坐标 白天自动生成的
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





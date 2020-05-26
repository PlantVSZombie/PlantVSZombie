import pygame
import sys
from Model.PeaShooter import PeaShooter
from Model.Zombie import Zombie
from Model.Zone import Zone
from Model.Bullet import Bullet
from Model.wallnut import  WallNut
from Model.sunfolwer import SunFlower





if __name__ == '__main__':
    zone=Zone()

    zombieList=[]
    zombie = Zombie(7)
    zombieList.append(zombie)
    zombie1 = Zombie(8)
    zombieList.append(zombie1)
    zombie2 = Zombie(9)
    zombieList.append(zombie2)

    wallnutList=[]
    sunflowerList=[]
    plantList=[]
    peashooter=PeaShooter(6,0)
    wallnut=WallNut(6,1)
    sunflower=SunFlower(5,1)
    plantList.append(peashooter)
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
            zombie.attack(wallnutList)
            zombie.attack(sunflowerList)
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




        pygame.display.update()
        index+=1
        #实现右上角关闭
        for event in pygame.event.get():
            # x,y=pygame.mouse.get_pos()
            # if event.type==pygame.MOUSEMOTION:
            #     print(zone.getIndex(x,y))


            if event.type==pygame.QUIT:
                sys.exit()





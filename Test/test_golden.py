import pygame
import sys

from Model.sunfolwer import SunFlower

screen_size=(1200,600)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption('郑祺琛的house')
img_background_path='../resources/pics/items/Background_0.jpg'
backGroup=pygame.image.load(img_background_path).convert()
display_index=0
block=pygame.time.Clock()
sunFlowerList=[]
sunflower = SunFlower(5, 1)
sunFlowerList.append(sunflower)
pygame.init()
isgolden=True
while True:
    block.tick(15)
    # #绘制背景

    screen.blit(backGroup, (0, 0))

    for sunflower in sunFlowerList:
        # if display_index % 18 == 16:
        #     if sunflower.times == 5:
        #         sun = sunflower.produce()  # 要添加向日葵变金色，可在类里
        #         sunflower.times = 0
        #         isgolden = True
        #         screen.blit(sunflower.golden[0], sunflower.rect)
        #     else:
        #         sunflower.times += 1
        #         screen.blit(sunflower.images[display_index % 17], sunflower.rect)
        # elif display_index % 18 == 17 and isgolden==True:
        #     screen.blit(sunflower.golden[1], sunflower.rect)
        #     isgolden = False
        # else:
        #     screen.blit(sunflower.images[display_index % 17], sunflower.rect)
        screen.blit(sunflower.golden[1], sunflower.rect)
        if sunflower.isAlive() == False:
            sunFlowerList.remove(sunflower)
    pygame.display.update()



    display_index += 1


    # 实现右上角关闭
    for event in pygame.event.get():
        # x,y=pygame.mouse.get_pos()
        # if event.type==pygame.MOUSEMOTION:
        #     print(zone.getIndex(x,y))

        if event.type == pygame.QUIT:
            sys.exit()

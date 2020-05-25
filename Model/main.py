import pygame
import sys
from Model.PeaShooter import PeaShooter
from Model.Zombie import Zombie





if __name__ == '__main__':

    zombie=Zombie()
    peashooter=PeaShooter()
    block=pygame.time.Clock()
    pygame.init()
    screen_size=(1200,600)
    screen=pygame.display.set_mode(screen_size)
    pygame.display.set_caption('郑祺琛的house')
    img_background_path='../resources/pics/items/Background_0.jpg'
    backGroup=pygame.image.load(img_background_path).convert()
    index=0
    while True:

        block.tick(15)
        #绘制背景
        screen.blit(backGroup,(0,0))
        screen.blit(peashooter.images[index%13],peashooter.rect)
        screen.blit(zombie.images[index % 14], zombie.rect)
        zombie.move()


        pygame.display.update()
        index+=1
        #实现右上角关闭
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()





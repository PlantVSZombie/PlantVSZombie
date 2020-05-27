import pygame
from sys import exit
from Controller import Controller
from View.Component.Button import Button
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PIC_FIRSTMENU_BACKGROUND_PATH, PIC_FIRSTMENU_ADVENBUTTON0_PATH, \
    PIC_FIRSTMENU_ADVENBUTTON1_PATH

'''返回Font对象'''
def  drawText(content):
    pygame.font.init()
    font  =  pygame.font.SysFont('SimHei',40)
    text  =  font.render(content,True,pygame.Color(0,0,0))
    return  text

def menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("测试主菜单")
    block = pygame.time.Clock()

    background = pygame.image.load( PIC_FIRSTMENU_BACKGROUND_PATH).convert_alpha()
    button = Button(650,100,PIC_FIRSTMENU_ADVENBUTTON0_PATH,PIC_FIRSTMENU_ADVENBUTTON1_PATH)
    while True:
        block.tick(15)
        screen.blit(background, (0, 0))
        x, y = pygame.mouse.get_pos()
        mouse_click, _, _ = pygame.mouse.get_pressed()
        if(button.isClicked(mouse_click,(x,y))):
           controller=Controller.Controller(screen)
           pygame.quit()
           exit()
           break    #为了让他别再循环了
        button.draw(screen)
        screen.blit(drawText("刘宗游 葛伟平"),(690,280))
        screen.blit(drawText("郑祺琛 郑汉亚"), (690, 360))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

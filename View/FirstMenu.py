import pygame

from View.Component.Button import Button
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PIC_FIRSTMENU_BACKGROUND_PATH, PIC_FIRSTMENU_ADVENBUTTON0_PATH, \
    PIC_FIRSTMENU_ADVENBUTTON1_PATH


def menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("测试主菜单")
    block = pygame.time.Clock()

    background = pygame.image.load("../" + PIC_FIRSTMENU_BACKGROUND_PATH).convert_alpha()
    button = Button(650,100,"../"+PIC_FIRSTMENU_ADVENBUTTON0_PATH,"../"+PIC_FIRSTMENU_ADVENBUTTON1_PATH)
    while True:
        block.tick(15)
        screen.blit(background, (0, 0))
        x, y = pygame.mouse.get_pos()
        mouse_click, _, _ = pygame.mouse.get_pressed()
        button.isClicked(mouse_click,(x,y))
        button.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

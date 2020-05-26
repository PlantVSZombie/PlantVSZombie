import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("测试主菜单")
    block = pygame.time.Clock()

    while True:
        block.tick(15)
        screen.fill([255, 255, 255])

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



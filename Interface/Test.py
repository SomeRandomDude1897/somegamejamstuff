import pygame
import sys
from Interface import Interface

pygame.init()

screen_width, screen_height = 720, 720
main_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Interface Example")

# Сделать начальный экран + переход к игре по кнопочке?ы

interface = Interface()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            interface.click_buttons(pygame.mouse.get_pos())

    main_screen.fill((255, 255, 255))

    for button in interface.buttons:
        button.draw(main_screen)

    pygame.display.flip()

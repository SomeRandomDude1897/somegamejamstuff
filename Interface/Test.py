import pygame
import sys
from Interface import Interface
from StartScreen import StartScreen

pygame.init()

screen_width, screen_height = 720, 720
main_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SomeGameJamStuff")


def start_game():
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


interface = Interface()
start_screen = StartScreen('Overlay.png', start_game)
start_screen.show(main_screen)

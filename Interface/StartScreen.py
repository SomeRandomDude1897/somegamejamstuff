import pygame
from Button import Button

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class StartScreen:
    def __init__(self, image_path, play_callback):
        self.width = 720
        self.height = 720
        self.background = pygame.image.load(image_path)
        self.play_button = Button(self.width // 2 - 75, self.height // 2 - 20, 150, 40, 'Options.png', play_callback)
        self.visible = True

    def show(self, screen):
        while self.visible:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.visible = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    self.play_button.process_click(pos)
                    if self.play_button.is_clicked(pos):
                        self.visible = False

            self.draw_start_screen(screen)
            pygame.display.flip()

    def draw_start_screen(self, screen):
        screen.blit(self.background, (0, 0))

        # Draw the "Play" button
        self.play_button.draw(screen)

        pygame.display.flip()

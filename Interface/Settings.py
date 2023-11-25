import pygame
from Button import Button
from Slider import Slider

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)


class Settings:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.rect = pygame.Rect(110, 110, self.width, self.height)

        self.volume_label = pygame.font.Font(None, 36).render("Volume", True, BLACK)

        self.sliders = [
            Slider(self.rect.left + 125, self.rect.top + 23, 200, 20)
        ]

        self.buttons = [
            Button(self.rect.left + 20, self.rect.top + 450, 150, 40, 'Options.png', self.close_settings),
        ]

        self.visible = False

    def open(self):
        self.visible = True

        while self.visible:
            self.handle_events()
            self.draw_window()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.visible = False
                return

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                for button in self.buttons:
                    button.process_click(pos)

                for slider in self.sliders:
                    if slider.is_clicked(pos):
                        slider.dragging = True
                    slider.update_value(pos)

            elif event.type == pygame.MOUSEMOTION:
                for slider in self.sliders:
                    if slider.dragging:
                        pos = pygame.mouse.get_pos()
                        slider.update_value(pos)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for slider in self.sliders:
                    slider.dragging = False

    def draw_window(self):
        # Окно настроек
        settings_surface = pygame.Surface((self.width, self.height))
        settings_surface.fill(GRAY)
        # Чёрная рамка
        pygame.draw.rect(settings_surface, BLACK, (0, 0, self.width, self.height), 2)

        # Рисуем слайдеры
        settings_surface.blit(self.volume_label, (10, 20))
        for slider in self.sliders:
            slider.draw(settings_surface, x_offset=self.rect.left, y_offset=self.rect.top)

        # Рисуем кнопочки в окне
        for button in self.buttons:
            button.draw(settings_surface, x_offset=self.rect.left, y_offset=self.rect.top)

        # Центруем окно настроек внутри основного
        main_surface = pygame.display.get_surface()
        main_surface.blit(settings_surface, (self.rect.left, self.rect.top))
        pygame.display.flip()

    def close_settings(self):
        self.visible = False

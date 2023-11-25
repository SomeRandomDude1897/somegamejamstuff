import pygame


class Button:
    def __init__(self, x, y, width, height, image_path, action=None):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))  # TEST
        self.action = action

        self.rect = pygame.Rect(x, y, width, height)

    def __is_clicked(self, pos):
        """Проверяет, попала ли точка в прямоугольник"""
        return self.rect.collidepoint(pos)

    def process_click(self, pos):
        if self.__is_clicked(pos) and self.action:
            self.action()

    def draw(self, surface, x_offset=0, y_offset=0):
        surface.blit(self.image, (self.rect.left - x_offset, self.rect.top - y_offset))

import pygame


class Slider:
    def __init__(self, x, y, width, height):
        self.min_value, self.max_value = 0, 100
        self.value = 50
        self.is_dragged = False

        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, x_offset=0, y_offset=0):
        pygame.draw.rect(surface, (100, 100, 100), self.rect.move(-x_offset, -y_offset))  # Apply offsets here
        knob_x = int((self.value - self.min_value) / (self.max_value - self.min_value) * (self.rect.width - 10))
        knob_rect = pygame.Rect(self.rect.left + knob_x, self.rect.top, 10, self.rect.height)
        pygame.draw.rect(surface, (0, 0, 0), knob_rect.move(-x_offset, -y_offset))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def update_value(self, pos):
        if not self.is_clicked(pos):
            return

        x_relative = pos[0] - self.rect.left  # Вычисляем отметку относительно 0 слайдера
        normalized_value = x_relative / self.rect.width  # Считаем процент, затем добавляем
        self.value = int(self.min_value + normalized_value * (self.max_value - self.min_value))

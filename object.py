from animation import Animation
import pygame

class Object():
    def __init__(self, start_x, start_y, width, heigth, is_threat, idle_animation):
        self.x = start_x
        self.y = start_y
        self.width = width
        self.height = heigth
        self.is_threat = is_threat # я чет подумал так наверное проще будет, и дальше можно в игроке обработать с чем он столкнулся
        self.left = self.right = False    # по умолчанию — стоим
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.idle_animation = idle_animation
    def GetSprite(self):
        sprite = self.idle_animation.GetFrame()
        # print(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.idle_animation.MoveFrame()
        return sprite
    def GetRect(self):
        return self.rect
    def UpdateRect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def Collide(self):
        return
    def Rotate(self):
        return
    def GetCoord(self):
        return (self.x, self.y)
    def Draw(self, screen):
        screen.blit(self.GetSprite(), self.GetCoord())

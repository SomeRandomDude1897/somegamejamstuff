from animation import Animation
import pygame

class Object:
    def __init__(self, start_x, start_y, width, heigth, is_threat, idle_animation):
        self.x = start_x
        self.y = start_y
        self.width = width
        self.height = heigth
        self.is_threat = is_threat # я чет подумал так наверное проще будет, и дальше можно в игроке обработать с чем он столкнулся
        self.rect = idle_animation.GetFrame().get_rect()
        self.idle_animation = idle_animation
    def GetSprite(self):
        sprite = self.idle_animation.GetFrame()
        self.idle_animation.MoveFrame()
        return sprite
    def GetRect(self):
        return self.rect
    def Collide(self):
        return
    def Rotate(self):
        return
    def GetCoord(self):
        return (self.x, self.y)
    def Draw(self, screen):
        screen.blit(self.GetSprite(), self.GetCoord())

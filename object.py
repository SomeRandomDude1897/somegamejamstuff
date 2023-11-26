from animation import Animation
from pygame import *
class Object:
    def __init__(self, start_x, start_y, width, heigth, is_threat, idle_animation):
        self.x = start_x
        self.y = start_y
        self.width = width
        self.heidth = heigth
        self.rect = Rect(start_x, start_y, width, heigth)
        self.rect.center = self.GetCoord()
        self.idle_animation = idle_animation
        self.is_threat = is_threat
    def Draw(self, screen):
        self.UpdateRect()
        screen.blit(self.idle_animation.GetFrame(), self.rect)
    def GetCoord(self):
        return (self.x + self.width/2, self.y + self.heidth/2)
    def GetSize(self):
        return (self.width, self.heidth)

    def GetSprite(self):
        sprite = self.idle_animation.GetFrame()
        self.idle_animation.MoveFrame()
        return sprite
    def GetRect(self):
        return self.rect
    def UpdateRect(self):
        self.rect = Rect(self.x, self.y, self.width, self.heidth)
        self.rect.center = self.GetCoord()
    def Collide(self):
        return
    def Rotate(self):
        return
    def MoveObj(self):
        return

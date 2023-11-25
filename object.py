from animation import Animation
from pygame import *

class Object(sprite.Sprite):
    def __init__(self, start_x, start_y, width, heigth, is_threat, idle_animation):
        self.width = width
        self.heidth = heigth
        self.rect = Rect(start_x, start_y, width, heigth)
        self.idle_animation = idle_animation
        self.is_threat = is_threat
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
    def MoveObj(self):
        return

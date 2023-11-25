from animation import Animation
from pygame import *

class Object(sprite.Sprite):
    def __init__(self, start_x, start_y, width, heigth, idle_animation):
        self.x = start_x
        self.y = start_y
        self.width = width
        self.heidth = heigth
        self.rect = Rect(start_x, start_y, width, heigth)
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

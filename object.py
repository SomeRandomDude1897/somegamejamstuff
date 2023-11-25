from animation import Animation
from pygame import *

class Object:
    def __init__(self, start_x, start_y, width, heigth, is_threat, idle_animation):
        self.x = start_x
        self.y = start_y
        self.width = width
        self.heidth = heigth
        self.rect = idle_animation.GetFrame().get_rect()
        self.is_threat = is_threat # я чет подумал так наверное проще будет, и дальше можно в игроке обработать с чем он столкнулся
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

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    def GetSprite(self):
        sprite = self.idle_animation.GetFrame()
        self.idle_animation.MoveFrame()
import pygame
from object import Object
class Player(Object):
    def __init__(self, start_x, start_y, width, heigth, idle_animation):
        Object.__init__(self, start_x, start_y, width, heigth, idle_animation)
        self.x_velocity = 0
        self.y_velocity = 0
        self.alive = True
    def GetAlive(self):
        return self.alive
    def Collide(self):
        return
    def Move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
    def AddForce(self, x_delta, y_delta):
        self.x_velocity += x_delta
        self.y_velocity += y_delta
    def GetRect(self):
        return self.rect
    
    def collide(self, xvel, yvel, objects):
        for p in objects:
            if pygame.sprite.collide_rect(self, p): # если есть пересечение платформы с игроком

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.onGround = True          # и становится на что-то твердое
                    self.yvel = 0                 # и энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает


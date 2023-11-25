import pygame
from object import Object
class Player(Object):
    def __init__(self, start_x, start_y, width, heigth, is_threat, idle_animation):
        Object.__init__(self, start_x, start_y, width, heigth, is_threat, idle_animation)
        self.x_velocity = 0
        self.y_velocity = 0
        self.alive = True
    def GetAlive(self):
        return self.alive
    def Collide(self):
        return
    def Move(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
    def AddForce(self, x_delta, y_delta):
        self.x_velocity += x_delta
        self.y_velocity += y_delta
    def GetRect(self):
        return self.rect
    
    def collide(self, object):
        if pygame.sprite.collide_rect(self, object): # если есть пересечение платформы с игроком
            if object.is_threat:
                self.alive = False

            if self.rect.top - self.heidth < object.rect.top:                      # если падает вниз
                self.rect.bottom = object.rect.top # то не падает вниз
  
            elif self.rect.bottom + self.heidth > object.rect.bottom :                      # если движется вверх
                self.rect.top = object.rect.bottom # то не движется вверх

            elif self.rect.right > object.rect.left:                      # если движется вправо
                self.rect.right = object.rect.left # то не движется вправо

            elif self.rect.left < object.rect.right:                      # если движется влево
                self.rect.left = object.rect.right # то не движется влево



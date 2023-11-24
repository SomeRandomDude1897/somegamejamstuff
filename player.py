import pygame
from object import Object
class Player(Object):
    def __init__(self, start_x, start_y, width, heigth, idle_animation):
        Object.__init__(self, start_x, start_y, width, heigth, False, idle_animation)
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
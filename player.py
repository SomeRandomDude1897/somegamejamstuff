import pygame
from object import Object
class Player(Object):
    def __init__(self, start_x, start_y, width, heigth, idle_animation):
        Object.__init__(self, start_x, start_y, width, heigth, False, idle_animation)
        '''скорость и дельта будет зависеть от размера карты'''
        self.x_velocity = 0
        self.y_velocity = 0
        self.alive = True
        self.x_delta = 0
        self.y_delta = 0
    def GetAlive(self):
        return self.alive
    def Collide(self):
        '''уже есть в родительском классе'''
        return
    def Move(self, move_right):
        '''move_right - bool значение, отвечающее за направление движения вправо'''
        if move_right:
            self.x += self.x_velocity
        else:
            self.x -= self.x_velocity
    def jump(self):

    def AddForce(self):
        '''для плавности движения'''
        self.x_velocity += x_delta
        self.y_velocity += y_delta
    def GetRect(self):
        '''уже есть в родительском классе'''
        return self.rect
    def draw(self):
        


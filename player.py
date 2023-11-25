# import pygame
import math
import time
from object import Object


class Player(Object):
    def __init__(self, start_x, start_y, width, heigth, idle_animation):
        Object.__init__(self, start_x, start_y, width, heigth, False, idle_animation)
        '''скорость и дельта будут зависеть от размера карты'''
        self.base_x_velocity = 0
        self.base_y_velocity = 0
        self.x_velocity = 0
        self.y_velocity = 0
        self.alive = True
        self.x_delta = 0
        self.y_delta = 0
        self.x = start_x
        self.y = start_y
        self.max_jump_height = 0

    def GetAlive(self):
        return self.alive

    def Move(self, move_right):
        '''move_right - bool значение, отвечающее за направление движения вправо
        от времени будет зависеть его скорость, разгон по времени планируется 1 секунда'''
        start = time.time()
        if start < 1:
            self.x_velocity = self.base_x_velocity * start
        else:
            self.x_velocity = self.base_x_velocity
        if move_right:
            self.x += self.x_velocity
        else:
            self.x -= self.x_velocity

    def Jump(self):
        '''проблема, как понять, когда нужно остановиться уменьшать координату по y, т.к.
        неизвестно, где приземлится персонаж'''
        prev_y = self.y
        start = time.time()
        g = 9.81 # условно такое будет ускорение
        stop_jumping = True
        while not stop_jumping: # прыжок с положительной скоростью
            self.y_velocity = self.base_y_velocity - g*(start)**2//2
            self.y += self.base_y_velocity
            # действие по изменению stop_jumping
        self.y_velocity = 0

    def ResetXVelocity(self):
        '''если персонаж уперся в стенку'''
        self.x_velocity = 0

    def ResetYVelocity(self):
        '''если персонаж уперся в потолок (должен будет вызываться и при прыжке)'''
        self.y_velocity = 0

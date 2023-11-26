from object import Object


class Player(Object):
    def __init__(self, start_x, start_y, width, heigth, idle_animation):
        Object.__init__(self, start_x, start_y, width, heigth, False, idle_animation)
        '''скорость и дельта будут зависеть от размера карты'''
        self.base_x_velocity = 4
        self.base_y_velocity = 4
        self.jump_power = 6
        self.x_velocity = 0
        self.y_velocity = 0
        self.alive = True
        self.x_delta = 0
        self.y_delta = 0
        self.g = 9.81
        self.max_jump_height = 0
        self.stand_on_ground = False
        self.collide_os_side = False
    def GetStand(self):
        return self.stand_on_ground
    def SetStand(self, value):
        self.stand_on_ground = value
        return self.stand_on_ground

    def GetAlive(self):
        return self.alive

    def SetAlive(self, isAlive):
        self.alive = isAlive
    def SetMoveVelocity(self, timeMoving):
        if timeMoving < 1:
            self.x_velocity = self.base_x_velocity * timeMoving
        else:
            self.x_velocity = self.base_x_velocity
    def MoveX(self, moveRight):
        if moveRight:
            self.x += self.x_velocity
        else:
            self.x -= self.x_velocity
    def MoveY(self):
        self.y += self.y_velocity

    def Falling(self, timeMoving):
        '''свободное падение персонажа'''
        self.y_velocity += 0.1
    def Jump(self):
        '''после вызова jump нужно вызввать MoveY, пока не столкнется снизу с поверхностью'''
        self.y_velocity = -self.jump_power

    def ResetXVelocity(self):
        '''если персонаж уперся в стенку'''
        self.x_velocity = 0

    def ResetYVelocity(self):
        '''если персонаж уперся в потолок (должен будет вызываться и при прыжке)'''
        self.y_velocity = 0

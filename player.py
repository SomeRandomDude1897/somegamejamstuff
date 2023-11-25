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
        self.g = 9.81
        self.max_jump_height = 0

    def GetAlive(self):
        return self.alive

    def SetAlive(self, isAlive):
        self.alive = isAlive

    def MoveX(self, moveRight, timeMoving):
        '''moveRight - bool значение, отвечающее за направление движения вправо
        от времени будет зависеть его скорость, разгон по времени планируется 1 секунда
        timeMoving - извне получать сколько времени уже двигается персонаж'''
        if timeMoving < 1:
            self.x_velocity = self.base_x_velocity * timeMoving
        else:
            self.x_velocity = self.base_x_velocity
        if moveRight:
            self.x += self.x_velocity
        else:
            self.x -= self.x_velocity

    def Falling(self, timeMoving):
        '''свободное падение персонажа'''
        self.y_velocity -= self.g * (timeMoving) ** 2 // 2
        self.y += self.y_velocity

    def Jump(self):
        '''после вызова jump нужно вызввать MoveY, пока не столкнется снизу с поверхностью'''
        self.y_velocity = self.base_y_velocity
        self.Falling(0)

    def ResetXVelocity(self):
        '''если персонаж уперся в стенку'''
        self.x_velocity = 0

    def ResetYVelocity(self):
        '''если персонаж уперся в потолок (должен будет вызываться и при прыжке)'''
        self.y_velocity = 0

from object import Object
class MovingObject(Object):
    def __init__(self, start_x, start_y, width, heigth, idle_animation, to_x, to_y): # мб имеет смысл придумать что-то типа класса точки в пространстве чисто чтобы удобнее x и y хранить
        Object.__init__(self, start_x, start_y, width, heigth, idle_animation)
        self.from_x = self.rect.x
        self.from_y = self.rect.y
        self.to_x = self.rect.x + to_x
        self.to_y = self.rect.y + to_y
        self.move_x = 7

    def GetSprite(self):
        self.rect.x += self.move_x

        if self.rect.x >= self.to_x or self.rect.x <= self.from_x:
            self.move_x = -self.move_x

        sprite = self.idle_animation.GetFrame()
        self.idle_animation.MoveFrame()
        return sprite
    

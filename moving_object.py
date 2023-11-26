from object import Object
class MovingObject(Object):
    def __init__(self, start_x, start_y, width, heigth, is_threat, idle_animation, to_x, to_y): # мб имеет смысл придумать что-то типа класса точки в пространстве чисто чтобы удобнее x и y хранить
        Object.__init__(self, start_x, start_y, width, heigth, is_threat, idle_animation)
        self.from_x, self.to_x = sorted([self.rect.x, self.rect.x + to_x])
        self.from_y, self.to_y = sorted([self.rect.y, self.rect.y + to_y])
        self.move_x = 7
        self.move_y = 7


    def GetSprite(self):
        sprite = self.idle_animation.GetFrame()
        self.idle_animation.MoveFrame()
        return sprite
    
    def MoveObj(self):
        if self.rect.x + self.move_x >= self.from_x and self.rect.x + self.move_x <= self.to_x:
            self.rect.x += self.move_x
        else:
            self.move_x = -self.move_x
        
        if self.rect.y + self.move_y >= self.from_y and self.rect.y + self.move_y <= self.to_y:
            self.rect.y += self.move_y
        else:
            self.move_y = -self.move_y
        
    

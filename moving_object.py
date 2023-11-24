from object import Object
class MovingObject(Object):
    def __init__(self, start_x, start_y, from_x, from_y,to_x, to_y): # мб имеет смысл придумать что-то типа класса точки в пространстве чисто чтобы удобнее x и y хранить
        Object.__init__(self, start_x, start_y)
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y

    # ну и дальше чета какие-то методы его движения

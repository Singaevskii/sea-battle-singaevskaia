
class Ship:
    def __init__(self, long, x, y, direction, quantity_of_life):
        self.y = y
        self.x = x
        self.direction = direction
        self.quantity_of_life = quantity_of_life
        self.long = long
    def get_long(self):
        return self.long
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_direction(self):
        return self.direction
    def get_quantity_of_life(self):
        return self.quantity_of_life

    def set_long(self,long):
        self.long=long
    def set_x(self,x):
        self.x=x
    def set_y(self,y):
        self.y=y
    def set_direction(self,direction):
        self.direction=direction
    def set_quantity_of_life(self,quantity_of_life):
        self.quantity_of_life=quantity_of_life



    def dots_check(self):
        global dots
        if self.direction == "upright":
            if self.long == 1:
                dots = [self.x, self.y]
            elif self.long == 2:
                dots = [self.x, self.y], [self.x, self.y + 1]
            elif self.long == 2:
                dots = [self.x, self.y], [self.x, self.y + 1], [self.x, self.y + 2]
        elif self.direction == 'horizon':
            if self.long == 1:
                dots = [self.x, self.y]
            elif self.long == 2:
                dots = [self.x, self.y], [self.x + 1, self.y]
            elif self.long == 2:
                dots = [self.x, self.y], [self.x + 1, self.y], [self.x + 2, self.y]
        return dots

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True

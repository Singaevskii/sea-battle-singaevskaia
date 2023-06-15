from exception import BoardOutException, BoardWrongShipException, BoardException, BoardUsedException
from Dots import Dot

class Ship:
    def __init__(self, bow: Dot, long, vertical: bool):
        self.bow = bow
        self.length = long
        self.vertical = vertical
        self.lives = long

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            curr_x = self.bow.x
            curr_y = self.bow.y
            if self.vertical:
                curr_y += i
            else:
                curr_x += i
            ship_dots.append(Dot(curr_x, curr_y))
        return ship_dots

    def is_hit(self, dot) -> bool:
        return dot in self.dots
from Ship import Ship
from exception import BoardOutException, ShipOutException
class Board(Ship):
    def __init__(self, board, ships, hid, live_ships, long, x, y, direction, quantity_of_life):
        super().__init__(long, x, y, direction, quantity_of_life)
        self.board = [[' ', '1', '2', '3', '4', '5', '6'],
                 ['1', 'O', 'O', 'O', 'O', 'O', 'O'],
                 ['2', 'O', 'O', 'O', 'O', 'O', 'O'],
                 ['3', 'O', 'O', 'O', 'O', 'O', 'O'],
                 ['4', 'O', 'O', 'O', 'O', 'O', 'O'],
                 ['5', 'O', 'O', 'O', 'O', 'O', 'O'],
                 ['6', 'O', 'O', '0', 'O', 'O', 'O']
                 ]
        self.ships=[]
        self.hid=True
        self.live_ships=6
    def add_ship(self,board,ships,x,y,direction):
        try:
            self.x = int(input("Введите координату коробля х: "))
            self.y = int(input("Введите координату коробля y: "))
            self.long = int(input("Введите длину коробля от 1 до 3: "))
            self.direction = str(input("Введите напраление коробля (upright or horizon): "))
            if (self.direction == 'upright' and self.x + self.long - 1 > 6) or (
                    self.direction == 'horizon' and self.y + self.long - 1 > 6) or self.long > 3 or self.long < 0 or (
                    self.direction != 'horizon' and self.direction != 'upright'):
                raise ShipOutException
        except ShipOutException:
            print("Недопустимые координаты для коробля: ")
        else:
            self.ships.append(self)


    def contour(self,x,y,direction,long):
        if self.direction=='horizontal':
            if x+long<7 :
                self.board[x+long][y]='#'
            if x-1>0:
                self.board[x-1][y]='#'
            if y+1<7:
                self.board[x][y+1]='#'
            if y-1>0:
                self.board[x][y-1]='#'









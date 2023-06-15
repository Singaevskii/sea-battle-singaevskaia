from Dots import Dot
from exception import BoardOutException, BoardWrongShipException, BoardUsedException


class Board:
    def __init__(self, size: int, hid=False):
        self.size = size
        self.hid = hid
        self.field = [['O'] * size for _ in range(size)]
        self.busy = []
        self.ships = []
        self.last_hit = []
        self.number_of_kills_ship = 0

    def __str__(self):
        res = '  | ' + ' | '.join(map(str, range(1, self.size + 1))) + ' |'
        for i, row in enumerate(self.field):
            res += f'\n{i + 1} | ' + ' | '.join(row) + ' |'
        if self.hid:
            res = res.replace('*', 'O')
        return res


    def out(self, d: Dot) -> bool:
        return not (0 <= d.x < self.size and 0 <= d.y < self.size)




    def contour(self, ship, visible=False):
        around = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
        for dot in ship.dots:
            for dx, dy in around:
                current_dots = Dot(dot.x + dx, dot.y + dy)
                if not self.out(current_dots) and current_dots not in self.busy:
                    if visible:
                        self.field[current_dots.x][current_dots.y] = '#'
                    self.busy.append(current_dots)

    '''Метод add_ship, который ставит корабль на доску (если ставить не получается, выбрасываем исключения).'''
    def add_ship(self, ship):
        for d in ship.dots:
            if d in self.busy or self.out(d):
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = '*'
            self.busy.append(d)
        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d: Dot) -> bool:
        if d in self.busy:
            raise BoardUsedException()
        if self.out(d):
            raise BoardOutException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.is_hit(d):
                self.field[d.x][d.y] = 'X'
                print('Попадание!')
                ship.lives -= 1
                if ship.lives == 0:
                    self.number_of_kills_ship += 1
                    self.contour(ship, visible=True)
                    print('Корабль уничтожен!')
                    self.last_hit = []
                    return False
                else:
                    print('Корабль ранен!')
                    self.last_hit.append(d)
                    return True

        self.field[d.x][d.y] = '.'
        print('Мимо!')
        return False

    def begin(self):
        self.busy = []

    def defeat(self):
        return self.number_of_kills_ship == len(self.ships)




'''Метод out, который для точки (объекта класса Dot) 
возвращает True, если точка выходит за пределы поля, и False, если не выходит.
'''


'''Метод contour, который обводит корабль по контуру. Он будет полезен и в ходе самой 
игры, и в при расстановке кораблей (помечает соседние точки, где корабля по правилам быть не может).'''
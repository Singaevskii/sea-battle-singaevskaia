from exception import BoardOutException, BoardWrongShipException, BoardException, BoardUsedException
from board import Board
from time import sleep
from Dots import Dot
from random import randint, choice
class Player:
    def __init__(self, board: Board, enemy: Board):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self) -> bool:    #возвращает True, если нужно ход повторить
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                sleep(1)
                return repeat
            except BoardException as excep:
                print(excep)

class AI(Player):
    def ask(self) -> Dot:
        last = self.enemy.last_hit
        while True:
            if last:    
                if len(last) == 1:
                    near = ((0, 1), (0, -1), (1, 0), (-1, 0))
                else:
                    if last[0].x == last[-1].x:
                        near = ((0, 1), (0, -1))
                    else:
                        near = ((1, 0), (-1, 0))
                dx, dy = choice(near)
                d = choice((Dot(last[-1].x + dx, last[-1].y + dy), Dot(last[0].x + dx, last[0].y + dy)))
            else:
                d = Dot(randint(0, 5), randint(0, 5))
            if d not in self.enemy.busy and not self.enemy.out(d):
                break
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')
        return d


class User(Player):
    def ask(self) -> Dot:
        while True:
            coords = input('Введите координаты выстрела:\t').split()
            if len(coords) != 2:
                print('Введите 2 координаты')
                continue
            x, y = coords
            if not all((x.isdigit(), y.isdigit())):
                print('Координаты должны быть числами')
                continue
            return Dot(int(x) - 1, int(y) - 1)


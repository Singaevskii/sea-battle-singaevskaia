from random import randint
from Dots import Dot
from Player import AI, User
from Ship import Ship
from board import Board
from exception import BoardWrongShipException


class Game:
    def __init__(self, size=6):
        self.lens = (3, 2, 2, 1, 1, 1, 1)
        self.size = size
        ai_board = self.random_board()
        user_board = self.random_board()
        ai_board.hid = True

        self.ai = AI(ai_board, user_board)
        self.pl = User(user_board, ai_board)

    def try_gen_board(self):
        attempts = 0
        board = Board(size=self.size)
        for l in self.lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), (randint(0, self.size))), l, bool(randint(0, 1)))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_gen_board()
        return board

    ''' метод, который в консоли приветствует пользователя и рассказывает о формате ввода.'''
    @staticmethod
    def greet():
        print("Игра началсь!")

    def print_boards(self):
        print('-' * self.size * 10)
        print('Ваша доска:'.ljust((self.size + 1) * 4 - 1) + ' ' * self.size + 'Доска компьютера:')
        for s1, s2 in zip(self.pl.board.__str__().split('\n'), self.ai.board.__str__().split('\n')):
            print(s1 + ' ' * self.size + s2)



    def loop(self):
        step = 0
        while True:
            self.print_boards()
            if step % 2 == 0:
                print('Вы ХОДИТЕ!')
                repeat = self.pl.move()
            else:
                print('Ходит компьютер!')
                repeat = self.ai.move()
            if repeat:
                step -= 1

            if self.ai.board.defeat():
                self.print_boards()
                print('Вы выиграли!')
                break
            if self.pl.board.defeat():
                self.print_boards()
                print('Компьютер выиграл!')
                break
            step += 1
    def start(self):
        self.greet()
        self.loop()

'''loop — метод с самим игровым циклом. Там мы просто последовательно вызываем метод 
mode для игроков и делаем проверку, сколько живых кораблей осталось на досках, чтобы определить победу.
start — запуск игры. Сначала вызываем greet, а потом loop.'''
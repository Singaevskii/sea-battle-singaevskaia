from Ship import Ship, Dot
from board import Board
from exception import BoardOutException, ShipOutException


def print_sea_field(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end="|")
        print()


sea_field = [[' ', '1', '2', '3', '4', '5', '6'],
             ['1', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['2', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['3', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['4', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['5', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['6', 'O', 'O', '0', 'O', 'O', 'O']
             ]

ROWS = 7
COLS = 7
GAME_OVER = True
LETS_PUT_SHIP_ON_THE_BOARD = True
ship_1 = 3
ship_2 = 2
ship_3 = 1


def check_number_of_ships():
    if ship_1 == 0 and ship_2 == 0 and ship_3 == 0:
        return False
    else:
        return True


def print_sea_field(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end="|")
        print()

    '''проверка на ввод координат, чтобы коробли не выходили за пределы доски'''




'''проверка на ввод координат, чтобы не координаты не заходили за пределы доски'''

print_sea_field(sea_field, ROWS, COLS)

while GAME_OVER:
    try:
        x = int(input("Введите координату х: "))
        y = int(input("Введите координату y: "))
        if x > 6 or x < 0 or y < 6 or y > 0:
            raise BoardOutException
    except BoardOutException:
        print("Неправильные координаты")

print_sea_field(sea_field, ROWS, COLS)

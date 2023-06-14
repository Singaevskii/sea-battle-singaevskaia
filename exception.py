class ShipOutException(Exception):
    "НЕдопустимые координаты для коробля, или введенено не допостимо направлниеб или недопутсимая длина"
    pass


class BoardOutException(Exception):
    "Недопустимая координаты,вышли за пределы доски"
    pass

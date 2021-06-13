from . import unit


class Knight(unit.Unit):
    id = 0
    name = "Рыцарь"
    attack = 5
    defence = 50
    cost = 100
    clonable = False
    curable = True

from . import unit


class Infantryman(unit.Unit):
    id = 0
    name = "Пехотинец"
    attack = 2
    defence = 20
    cost = 20
    clonable = True
    curable = True


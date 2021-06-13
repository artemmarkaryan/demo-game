import random
import army


class Unit:
    id = 0
    name = ""
    health = 100
    attack = 0
    defence = 0
    cost = 0
    clonable = False
    curable = True

    def __init__(self):
        self.id = random.randint(0, 100)

    def special_action(
            self,
            index: int,
            friends_army: army.Army,
            enemies_army: army.Army
    ):
        pass

    def __str__(self):
        return f"{self.name} #{self.id}"
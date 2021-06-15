from . import unit
import army


class Doctor(unit.Unit):
    id = 0
    name = "Доктор"
    attack = 4
    defence = 30
    cost = 30
    clonable = False
    curable = True
    special_action_probability = 0.5

    def special_action(
            self,
            index: int,
            friends_army: army.Army,
            enemies_army: army.Army
    ):
        s = []
        to_cure = []
        if index + 1 < len(friends_army):
            to_cure.append(friends_army[index + 1])
        if index - 1 > 0:
            to_cure.append(friends_army[index - 1])

        for u in to_cure:
            if u.curable:
                u.health += 10
                s.append(f"{u}: +10 к здоровью")

        return '\n'.join(s)
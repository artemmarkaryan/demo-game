from . import unit
import army


class Wizard(unit.Unit):
    id = 0
    name = "Волшебник"
    attack = 4
    defence = 100
    cost = 100
    clonable = False
    curable = True
    special_action_probability = 0.5

    def special_action(
            self,
            index: int,
            friends_army: army.Army,
            enemies_army: army.Army
    ):
        to_clone = []
        s = []
        if index+1 < len(friends_army):
            to_clone.append(friends_army[index+1])
        if index-1 > 0:
            to_clone.append(friends_army[index-1])

        u: unit.Unit
        for u in to_clone:
            if u.clonable:
                friends_army.append(u.clone())
                s.append(f"{u} клонирован")

        return '\n'.join(s)

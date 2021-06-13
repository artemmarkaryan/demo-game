import random
import army
from units import (
    infantryman,
    knight,
    doctor,
    wizard
)

possible_units = [
    infantryman.Infantryman,
    knight.Knight,
    doctor.Doctor,
    wizard.Wizard
]


def create_army(cost, name) -> army.Army:
    new_army = army.Army(name)
    while True:
        unit = random.choice(possible_units)
        if unit.cost > cost:
            break
        else:
            new_army.append(unit())
            cost -= unit.cost
    return new_army


def game():
    cost = int(input("Cost: "))
    army_1 = create_army(cost, "Красные")
    army_2 = create_army(cost, "Синие")

    army.print_armies(army_1, army_2)

    sides = [army_1, army_2]
    for i in range(1, 1 << 31 - 1):
        print(f"\nХод №{i}")
        side_1 = random.choice([0, 1])
        side_2 = abs(side_1 - 1)

        friends, enemies = sides[side_1], sides[side_2]
        if len(friends) > 0 and len(enemies) > 0:
            friends.attack(enemies)
            friends.trigger_special_actions(enemies)
        if len(friends) > 0 and len(enemies) > 0:
            enemies.attack(friends)
        if len(friends) == 0 or len(enemies) == 0:
            break

    for s in sides:
        if len(s) > 0:
            print(f"\nАрмия {s} выиграла")
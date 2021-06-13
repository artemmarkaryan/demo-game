import random
import pprint
import os

import army
from units import (
    infantryman,
    knight,
    doctor,
    wizard
)

pp = pprint.PrettyPrinter().pprint
possible_units = [
    infantryman.Infantryman,
    knight.Knight,
    doctor.Doctor,
    wizard.Wizard
]
game_snapshots = []


def game():
    cost = int(input("Стоимость армии: "))
    army_1 = army.Army(cost, "🔴 Красные", possible_units)
    army_2 = army.Army(cost, "🔵 Синие", possible_units)

    print(army_1)
    print(army_2)

    sides = [army_1, army_2]
    for i in range(1, 1 << 31 - 1):
        s = [f"\nХод №{i}"]
        actions = []
        side_1 = random.choice([0, 1])
        side_2 = abs(side_1 - 1)

        friends, enemies = sides[side_1], sides[side_2]
        if len(friends) > 0 and len(enemies) > 0:
            actions.append(friends.attack(enemies))
            special_action_string = friends.trigger_special_actions(enemies)
            if special_action_string != "":
                actions.append(special_action_string)
        if len(friends) > 0 and len(enemies) > 0:
            actions.append(enemies.attack(friends))
        if len(friends) == 0 or len(enemies) == 0:
            break

        actions = filter(lambda x: x != "", actions)
        s.append("🔫 Действия")
        s.extend(actions)
        s.append("📊 Состояние армий")
        s.append(str(army_1))
        s.append(str(army_2))
        game_snapshots.append("\n".join(s))

    i = 0
    print(game_snapshots[i])

    while True:
        if i == len(game_snapshots) - 1:
            print(game_snapshots[i])
            break

        inp = input("вперёд/назад (в/н): ")
        if inp == "в":
            i += 1
        elif inp == "н":
            i -= 1

        print(game_snapshots[i])

    for s in sides:
        if len(s) > 0:
            print(f"\nАрмия {s} выиграла")

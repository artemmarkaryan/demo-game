import random

class Army(list):
    name = ""

    def __init__(self, cost, name, possible_units):
        units = []
        while True:
            unit = random.choice(possible_units)
            if unit.cost > cost:
                break
            else:
                units.append(unit())
            cost -= unit.cost
        super().__init__()
        self.name = name
        self.extend(units)

    def attack(self, enemies):
        s = [f"{self[0]} атакует {enemies[0]}"]
        enemies[0].health -= self[0].attack

        if enemies[0].health <= 0:
            s.append(f"{enemies[0]} умер")
            enemies.pop(0)

        else:
            self[0].health -= enemies[0].attack
            if self[0].health <= 0:
                s.append(f"{self[0]} умер")
                self.pop(0)

        return "\n".join(s)

    def trigger_special_actions(self, enemies):
        s = []
        for i in range(1, len(self)):
            if random.random() > self[i].special_action_probability:
                action_string = self[i].special_action(
                    index=i,
                    friends_army=self,
                    enemies_army=enemies
                )
                if action_string is not None:
                    s.append(action_string)

        return "\n".join(s)

    def __str__(self):
        return f"{self.name}\n{self.units_repr()}"

    # def __repr__(self):
    #     return f"{self}\n{self.units_repr()}"

    def units_repr(self):
        return "\n".join(
            f"{u.name} #{u.id}; Здоровье: {u.health}" for u in self
        )

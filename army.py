class Army(list):
    name = ""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def attack(self, enemies):
        print(f"{self[0]} атакует {enemies[0]}")
        enemies[0].health -= self[0].attack

        if enemies[0].health <= 0:
            print(f"{enemies[0]} умер")
            enemies.pop(0)

        else:
            self[0].health -= enemies[0].attack
            if self[0].health <= 0:
                print(f"{self[0]} умер")
                self.pop(0)

    def trigger_special_actions(self, enemies):
        if len(self) <= 1:
            return

        for i in range(1, len(self)):
            self[i].special_action(
                index=i,
                friends_army=self,
                enemies_army=enemies
            )

    def __str__(self):
        return f"{self.name}"

    def units_repr(self):
        return "\n".join(
            f"{u.name} #{u.id}; Здоровье: {u.health}" for u in self
        )


def print_armies(friends: Army, enemies: Army):
    print(f'''
______________
{friends}
{friends.units_repr()}
______________
{enemies}
{enemies.units_repr()}
______________''')

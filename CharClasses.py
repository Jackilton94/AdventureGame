class Knight:
    def __init__(self, a, d, m, dx, hp):
        self.attack = a
        self.defence = d
        self.magic = m
        self.dexterity = dx
        self.hit_points = hp

    def knight_attack(self):
        damage = self.attack + Sword.sword_damage()

        return damage


class Barbarian:
    def __init__(self, a, d, m, dx, hp):
        self.attack = a
        self.defence = d
        self.magic = m
        self.dexterity = dx
        self.hit_points = hp


class Wizard:
    def __init__(self, a, d, m, dx, hp):
        self.attack = a
        self.defence = d
        self.magic = m
        self.dexterity = dx
        self.hit_points = hp


class Rogue:
    def __init__(self, a, d, m, dx, hp):
        self.attack = a
        self.defence = d
        self.magic = m
        self.dexterity = dx
        self.hit_points = hp



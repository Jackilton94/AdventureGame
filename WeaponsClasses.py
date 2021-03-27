class Sword:



    def __init__(self, d):
        self.damage = d

    def sword_damage(self, s):

        attack_damage = self.damage + s
        return attack_damage

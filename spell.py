from abc import ABC, abstractmethod

class Spell(ABC):
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self, caster):
        pass

class Fireball(Spell):
    def cast(self, caster):
        print(f"{caster.character_class} использует Огненный шар. Урон: {self.damage}")
        return self.damage

class IceLance(Spell):
    def cast(self, caster):
        print(f"{caster.character_class} использует Ледяное копьё. Урон: {self.damage}")
        return self.damage

class LightningBolt(Spell):
    def cast(self, caster):
        print(f"{caster.character_class} использует Молнию. Урон: {self.damage}")
        return self.damage
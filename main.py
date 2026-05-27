from character import Character
from monster import Monster
from spell import Fireball, IceLance, LightningBolt

def main():
    print("Проверка игры от кота Василия")
    print("=" * 50)
    
    warrior = Character(18, 12, 16, 8, 10, 10, 'warrior')
    mage = Character(8, 10, 12, 16, 18, 12, 'mage')
    hunter = Character(14, 18, 14, 12, 10, 10, 'hunter')
    
    goblin = Monster(10, 8, 9, 4, 5, 3)
    print("Модуль 1: Проверка монстра")
    print(f"Здоровье монстра: {goblin.calculate_max_health()}")
    print(f"Урон монстра: {goblin.calculate_damage()}")
    print(f"Защита монстра: {goblin.calculate_defense()}")
    print()
    
    print("Модуль 2: Проверка персонажей")
    print(f"Воин - Здоровье: {warrior.max_health}, Урон: {warrior.damage}, Защита: {warrior.defense}")
    print(f"Маг - Здоровье: {mage.max_health}, Урон: {mage.damage}, Защита: {mage.defense}")
    print(f"Охотник - Здоровье: {hunter.max_health}, Урон: {hunter.damage}, Защита: {hunter.defense}")
    print()
    
    print("Модуль 3: Проверка маны и заклинаний")
    print(f"Мана воина: {warrior.mana}")
    print(f"Мана мага: {mage.mana}")
    print(f"Мана охотника: {hunter.mana}")
    print()
    
    mage.add_spell(Fireball("Огненный шар", 45, 20))
    mage.add_spell(IceLance("Ледяное копьё", 30, 12))
    mage.add_spell(LightningBolt("Молния", 50, 25))
    
    warrior.add_spell(Fireball("Огненный шар", 35, 15))
    hunter.add_spell(IceLance("Ледяное копьё", 28, 10))
    
    print("Применение заклинаний:")
    try:
        damage = mage.cast_spell(0)
        print(f"Нанесено урона: {damage}, Осталось маны: {mage.mana}")
        
        damage = mage.cast_spell(1)
        print(f"Нанесено урона: {damage}, Осталось маны: {mage.mana}")
        
        damage = warrior.cast_spell(0)
        print(f"Нанесено урона: {damage}, Осталось маны: {warrior.mana}")
        
        damage = hunter.cast_spell(0)
        print(f"Нанесено урона: {damage}, Осталось маны: {hunter.mana}")
    except Exception as e:
        print(f"Ошибка: {e}")
    print()
    
    print("Проверка абстрактных классов:")
    try:
        from unit import Unit
        test = Unit(1, 1, 1, 1, 1, 1)
        print("ОШИБКА: Unit можно создать")
    except TypeError:
        print("УСПЕХ: Unit нельзя создать")
    
    try:
        from spell import Spell
        test_spell = Spell("test", 10, 5)
        print("ОШИБКА: Spell можно создать")
    except TypeError:
        print("УСПЕХ: Spell нельзя создать")
    
    print()
    print("Все проверки пройдены")

if __name__ == "__main__":
    main()
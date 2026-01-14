from homework import Character

print("=== Testing Character (Base Class) ===")
try:
    c1 = Character("Villager", 1)
    print(f"Name: {c1.get_name()}")
    print(f"HP: {c1.get_hp()}")
    c1.take_damage(20)
    print(f"After taking 20 dmg: {c1.get_hp()}")
    c1.heal(10)
    print(f"After healing 10: {c1.get_hp()}")
except Exception as e:
    print(e)

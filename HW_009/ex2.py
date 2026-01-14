from homework import Character, Warrior, Mage

print("=== Testing Warrior ===")
w1 = Warrior("Arthur", 10, 50)
dummy = Character("Dummy", 1)
print(w1)
w1.attack(dummy)
print(f"Dummy HP after attack: {dummy.get_hp()}")

print("\n=== Testing Mage ===")
m1 = Mage("Merlin", 10, 100)
dummy2 = Character("Dummy2", 5)
m1.attack(dummy2)
print(f"Dummy2 HP after weak attack: {dummy2.get_hp()}")
m1.cast_spell(dummy2, "Fireball")
print(f"Dummy2 HP after Fireball: {dummy2.get_hp()}")

from homework import Character, Warrior, Mage
import inspect

def test_rpg():
    print("=== Testing Character (Base Class) ===")
    try:
        c1 = Character("Villager", 1)
        
        # Check Encapsulation
        if hasattr(c1, 'hp') or hasattr(c1, 'name'):
            print("FAIL: 'hp' or 'name' should not be public attributes!")
        else:
            print("PASS: attributes are private/protected.")

        print(f"Name: {c1.get_name()}")
        print(f"HP: {c1.get_hp()}")
        
        c1.take_damage(20)
        print(f"After taking 20 dmg: {c1.get_hp()} (Expected 80)")
        
        c1.heal(10)
        print(f"After healing 10: {c1.get_hp()} (Expected 90)")
        
        c1.heal()
        print(f"After full heal: {c1.get_hp()} (Expected 100)")
        
    except Exception as e:
        print(f"Error in Character test: {e}")

    print("\n=== Testing Warrior (Inheritance & Override) ===")
    try:
        w1 = Warrior("Arthur", 10, 50) # Level 10, Strength 50
        dummy = Character("Dummy", 1)
        
        print(w1)
        # Check override
        w1.attack(dummy) # Should calculate damage
        print(f"Dummy HP after Warrior attack (expect < 100): {dummy.get_hp()}")
        
    except Exception as e:
        print(f"Error in Warrior test: {e}")

    print("\n=== Testing Mage (Polymorphism & Overload) ===")
    try:
        m1 = Mage("Merlin", 10, 100) # Level 10, Mana 100
        dummy2 = Character("Dummy2", 5)
        
        m1.attack(dummy2) # Weak attack
        print(f"Dummy2 HP after weak attack: {dummy2.get_hp()}")
        
        # Overload check
        m1.cast_spell(dummy2, "Fireball")
        print(f"Dummy2 HP after Fireball: {dummy2.get_hp()}")
        
        m1.cast_spell(dummy2) # Default spell logic if implemented? Instructions imply 'Fireball' default or just method exists
        # Instructions said: cast_spell(target, spell_name="Fireball")
        print("Cast spell default arg test passed (no crash).")
        
    except Exception as e:
        print(f"Error in Mage test: {e}")

    print("\n=== Testing Comparisons (Magic Methods) ===")
    try:
        c_low = Character("Rookie", 1)
        c_high = Character("Veteran", 50)
        
        if c_high > c_low:
             print("PASS: Veteran > Rookie")
        else:
             print("FAIL: Comparison logic incorrect")
             
    except Exception as e:
        print(f"Error in Comparison test: {e}")

if __name__ == "__main__":
    test_rpg()

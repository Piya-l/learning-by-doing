# RPG Character Adventure

In this assignment, you will build a core engine for a Role-Playing Game (RPG). You need to define how characters behave, fight, and grow.

## Instructions

Create a file named `homework.py` inside this folder.
Implement the following class hierarchy.

### 1. Class `Character` (Base Class)
This class represents any entity in the game world.

*   **Initialization (`__init__`)**:
    *   Accepts `name` (string) and `level` (int).
    *   Sets `hp` (Health Points) to `100` by default.
    *   **Constraints**:
        *   `name` and `hp` must be **strictly private** (not accessible directly from outside).
        *   `level` should be **protected** (accessible to subclasses).
*   **Accessors**:
    *   `get_name()`: Returns the name.
    *   `get_hp()`: Returns the current HP.
    *   `is_alive()`: Returns `True` if HP > 0, else `False`.
*   **Actions**:
    *   `take_damage(amount)`: Reduces HP by `amount`. HP cannot go below 0.
    *   `heal(amount=None)`:
        *   If `amount` is provided, increase HP by that amount.
        *   If `amount` is **NOT** provided, restore HP to fully `100`.
        *   HP cannot exceed 100.
    *   `attack(target)`:
        *   This method should raise `NotImplementedError("Subclasses must implement attack method")` to ensure it is overridden.
*   **Comparisons**:
    *   Implement logic so that `char1 > char2` checks if `char1`'s level is higher than `char2`'s level.
*   **Representation**:
    *   `print(character)` should show: `"Character: [Name], Lvl: [Level], HP: [HP]"`

### 2. Class `Warrior` (Inherits from `Character`)
A strong fighter who relies on physical strength.

*   **Initialization**:
    *   Accepts `name`, `level`, and `strength` (int).
    *   Initialize the parent class properly.
    *   Store `strength` as a protected attribute.
*   **Combat**:
    *   `attack(target)`:
        *   Damage is calculated as: `strength * 1.5`.
        *   Calls `target.take_damage(damage)`.
        *   Prints: `"[Name] swings sword at [Target Name] for [Damage] dmg!"`.
*   **Representation**:
    *   `print(warrior)` should show: `"Warrior: [Name], Lvl: [Level], STR: [Strength], HP: [HP]"`

### 3. Class `Mage` (Inherits from `Character`)
A spellcaster who generally uses magic but can also strike weakly.

*   **Initialization**:
    *   Accepts `name`, `level`, and `mana` (int).
    *   Initialize the parent class.
    *   Store `mana` as a protected attribute.
*   **Combat**:
    *   `attack(target)`:
        *   Standard attack (whacking with staff).
        *   Damage = `level * 1`.
        *   Calls `target.take_damage(damage)`.
        *   Prints: `"[Name] hits [Target Name] with staff for [Damage] dmg!"`.
    *   `cast_spell(target, spell_name="Fireball")`:
        *   **Mana Cost**: `10` mana.
        *   If not enough mana, print `"[Name] is out of mana!"` and do nothing.
        *   If `spell_name` is "Fireball": Damage = `level * 3`.
        *   If `spell_name` is "IceShard": Damage = `level * 2`.
        *   Reduce mana by 10.
        *   Call `target.take_damage(damage)`.
        *   Prints: `"[Name] casts [spell_name] on [Target Name] for [Damage] dmg!"`.

---

## Testing

Use `chk_homework.py` to verify your code.

### Expected Output Example
When running `chk_homework.py`, the output should look like this:

```text
=== Testing Character (Base Class) ===
PASS: attributes are private/protected.
Name: Villager
HP: 100
After taking 20 dmg: 80 (Expected 80)
After healing 10: 90 (Expected 90)
After full heal: 100 (Expected 100)

=== Testing Warrior (Inheritance & Override) ===
Warrior: Arthur, Lvl: 10, STR: 50, HP: 100
Arthur swings sword at Dummy for 75.0 dmg!
Dummy HP after Warrior attack (expect < 100): 25.0

=== Testing Mage (Polymorphism & Overload) ===
Merlin hits Dummy2 with staff for 10 dmg!
Dummy2 HP after weak attack: 90
Merlin casts Fireball on Dummy2 for 30 dmg!
Dummy2 HP after Fireball: 60
Merlin casts Fireball on Dummy2 for 30 dmg!
Cast spell default arg test passed (no crash).

=== Testing Comparisons (Magic Methods) ===
PASS: Veteran > Rookie
```

### Checklist
1.  All attributes like `__hp` must NOT be accessible like `hero.hp` or `hero.__hp`.
2.  `heal()` must work both with and without arguments.
3.  `>` operator must correctly compare levels.
4.  Subclasses must override behavior correctly.

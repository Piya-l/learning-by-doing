# Homework 9: RPG Character Adventure

In this assignment, you will build a core engine for a Role-Playing Game (RPG). You'll practice proper encapsulation with private, protected, and public members, inheritance, method overriding, and operator overloading.

## Instructions

Create a file named `homework.py` and implement the following class hierarchy.

## Class 1: `Character` (Base Class)

Represents any entity in the game world.

### Access Modifiers Requirements

**Private Attributes (use `__` prefix):**
- `__name` - character's name (strictly private, not accessible from outside)
- `__hp` - health points (strictly private)

**Protected Attributes (use `_` prefix):**
- `_level` - character level (accessible to subclasses)

### Initialization

```python
def __init__(self, name, level):
```

- Accept `name` (string) and `level` (int)
- Set `__hp` to 100 by default
- Store `__name` and `_level` with proper prefixes

### Public Methods (Accessors)

- `get_name()` - returns `__name`
- `get_hp()` - returns `__hp`
- `is_alive()` - returns `True` if `__hp > 0`, else `False`

### Public Methods (Actions)

**`take_damage(amount)`**
- Reduce `__hp` by amount
- HP cannot go below 0

**`heal(amount=None)`** - Method overloading with default parameter
- If `amount` provided: increase `__hp` by that amount
- If `amount` is `None`: restore `__hp` to 100
- HP cannot exceed 100

**`attack(target)`** - Must be overridden
- Raise `NotImplementedError("Subclasses must implement attack method")`
- This forces all subclasses to override this method

### Magic Methods (Operator Overloading)

**Comparison (`__gt__`):**
```python
char1 > char2  # True if char1._level > char2._level
```

**String Representation (`__str__`):**
```python
print(character)  # "Character: [Name], Lvl: [Level], HP: [HP]"
```

---

## Class 2: `Warrior` (Inherits from `Character`)

A strong fighter who relies on physical strength.

### Initialization

```python
def __init__(self, name, level, strength):
```

- Accept `name`, `level`, and `strength` (int)
- Call `super().__init__(name, level)` to initialize parent
- Store strength as **protected** attribute: `_strength`

### Method Overriding

**`attack(target)`** - Override the base class method
- Calculate damage: `_strength * 1.5`
- Call `target.take_damage(damage)`
- Print: `"[Name] swings sword at [Target Name] for [Damage] dmg!"`

### String Representation (Override)

```python
print(warrior)  # "Warrior: [Name], Lvl: [Level], STR: [Strength], HP: [HP]"
```

---

## Class 3: `Mage` (Inherits from `Character`)

A spellcaster who can use magic or weak physical attacks.

### Initialization

```python
def __init__(self, name, level, mana):
```

- Accept `name`, `level`, and `mana` (int)
- Call `super().__init__(name, level)` to initialize parent
- Store mana as **protected** attribute: `_mana`

### Method Overriding

**`attack(target)`** - Override for weak physical attack
- Damage = `_level * 1`
- Call `target.take_damage(damage)`
- Print: `"[Name] hits [Target Name] with staff for [Damage] dmg!"`

### Additional Method

**`cast_spell(target, spell_name="Fireball")`** - Method overloading with default
- Mana cost: 10
- Check if `_mana >= 10`:
  - If not enough: print `"[Name] is out of mana!"` and return
- Calculate damage based on `spell_name`:
  - "Fireball": damage = `_level * 3`
  - "IceShard": damage = `_level * 2`
- Reduce `_mana` by 10
- Call `target.take_damage(damage)`
- Print: `"[Name] casts [spell_name] on [Target Name] for [Damage] dmg!"`

---

## Access Control Summary

| Attribute | Modifier | Access Level |
|-----------|----------|--------------|
| `__name` | Private | Only inside `Character` class |
| `__hp` | Private | Only inside `Character` class |
| `_level` | Protected | `Character` and subclasses |
| `_strength` | Protected | `Warrior` and its subclasses |
| `_mana` | Protected | `Mage` and its subclasses |

**Important:** Direct access like `hero.__hp` or `hero.hp` should NOT work. Use getters.

---

## OOP Concepts Tested

1. **Encapsulation**: Private (`__`) and protected (`_`) attributes
2. **Inheritance**: `Warrior` and `Mage` inherit from `Character`
3. **Method Overriding**: Both override `attack()` and `__str__()`
4. **Method Overloading**: `heal(amount=None)`, `cast_spell(target, spell_name="Fireball")`
5. **Operator Overloading**: `__gt__` for `>` comparison, `__str__` for string representation
6. **Abstract Methods**: `attack()` in base class raises `NotImplementedError`

---

## Testing

Run `chk_homework.py` to verify your code.

Expected behavior:
- Private attributes like `__hp` cannot be accessed directly
- `heal()` works with and without arguments
- `>` operator compares levels correctly
- Subclasses override methods properly
- Protected attributes accessible in subclasses

## Submission

Submit `homework.py` via GitHub Classroom.

Your code must:
- Use `__` for private attributes (`__name`, `__hp`)
- Use `_` for protected attributes (`_level`, `_strength`, `_mana`)
- Override methods in subclasses
- Implement all magic methods

## Common Mistakes

- Forgetting `__` or `_` prefixes
- Not calling `super().__init__()` in subclasses
- Directly accessing private attributes instead of using getters
- Not implementing `NotImplementedError` in base `attack()`
- Forgetting to check mana before casting spell

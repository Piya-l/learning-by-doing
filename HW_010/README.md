# Galactic Droid Factory

You are a lead engineer at a droid manufacturing plant. You need to implement the core class structure for droids, ensuring they can be manufactured, upgraded, and decommissioned correctly.

## Instructions

Create a file named `homework.py` and implement the following.

### 1. Class `Droid` (Base Class)
*   **Class Level Data**:
    *   Maintain a count of all functional droids in the universe.
*   **Creation & Destruction**:
    *   **Construction (`__init__`)**:
        *   Accepts `name` (str) and `serial_number` (str).
        *   Sets `power_level` to `50` by default.
        *   **Validation**:
            *   Must check if `serial_number` is valid using a helper method (see below).
            *   If invalid, raise `ValueError` with message "Invalid serial number".
        *   Increment the population count of droids.
    *   **Decommissioning (`__del__`)**:
        *   When a droid instance is destroyed (garbage collected), decrement the population count.
        *   Print: `"[Name] ([Serial]) is being scrapped."`
*   **Representation**:
    *   String representation should be: `"Droid: [Name], S/N: [Serial], Power: [Power]"`
*   **Population Tracking**:
    *   Implement a method `get_population()` that returns the current total number of droids. This method should be callable **without** an instance.
*   **Utility**:
    *   Implement a method `verify_serial_code(code)` that checks if the serial code follows the format `"AZ-####"` (two uppercase letters, hyphen, four digits).
    *   This helper should be usable without creating any Droid instance.
*   **Comparisons**:
    *   `d1 == d2`: True if their `serial_number` is identical.
    *   `d1 > d2`: True if `d1` has a higher `power_level` than `d2`.
*   **Upgrades (`+` operator)**:
    *   `d1 + d2`: Fusion!
    *   Returns a **NEW** `Droid` object.
    *   New Name: `d1.name` + "-" + `d2.name`
    *   New Serial: `d1.serial` + "-" + `d2.serial`
    *   New Power: `d1.power` + `d2.power` (Capped at 100).
    *   **Note**: The two old droids are untouched (immutable operation).

### 2. Class `ProtocolDroid` (Inherits from `Droid`)
*   **Behavior**:
    *   **Custom Initialization**:
        *   Accepts `name`, `serial_number`, and `languages` (list of strings).
        *   Power level starts at `20` (they are not fighters).
    *   **Representation**:
        *   Overrides parent to show: `"Protocol Droid: [Name], Languages: [Count]"`
    *   **Task Execution**:
        *   Method `translate(phrase, language=None)`:
            *   If `language` is None, print: `"Translating '[phrase]' to all known languages."`
            *   If `language` is provided and known, print: `"Translating '[phrase]' to [language]."`
            *   If `language` is provided but NOT known, print: `"Language [language] not supported."`

### 3. Class `FactoryAI` (Singleton Pattern)
*   **Behavior**:
    *   This class represents the central AI controlling the factory.
    *   **Singleton Requirement**:
        *   Ensure that **only one instance** of `FactoryAI` can ever exist.
        *   If a user tries to create a second instance `FactoryAI()`, return the **same** original instance.
        *   Hint: Override `__new__`.
    *   **Methods**:
        *   `__init__(self)`: Print `"Factory AI initializing..."` only once (if possible) or every time `__init__` is called (but `__new__` ensures same object).
        *   `authorize_production(self)`: Returns `True`. Print `"Production authorized via [hex id of self]"`.

---

## Testing

Use `chk_homework.py` to verify your code.
Your code must demonstrate correct usage of class-level vs instance-level data and methods.

### Expected Output Example
```text
=== 1. Testing Static & Class Methods ===
PASS: verify_serial_code works.
Initial Population: 0

=== 2. Testing Creation & Validation ===
PASS: correctly rejected invalid serial.
Droid: Alpha, S/N: AZ-0001, Power: 50
Droid: Beta, S/N: AZ-0002, Power: 50
Current Population: 2 (Expected 2)

=== 3. Testing Magic Methods (Comparisons & Operators) ===
PASS: d2 != d3
PASS: 50 is not > 50
Fused Droid: Droid: Alpha-Beta, S/N: AZ-0001-AZ-0002, Power: 100
PASS: Fusion droid is stronger.

=== 4. Testing Inheritance & Access ===
Protocol Droid: C-3PO, Languages: 2
Translating 'Hello' to all known languages.
Translating 'Hola' to English.
Language Sith not supported.

=== 5. Testing Destruction (Simulated) ===
Deleting d2...
Beta (AZ-0002) is being scrapped.
Alpha-Beta (AZ-0001-AZ-0002) is being scrapped.
Population after delete (approx): 1

=== 6. Testing Singleton (FactoryAI) ===
FactoryAI initializing...
Production authorized via 0x1023...
FactoryAI initializing...
PASS: ai1 and ai2 are the SAME object.
```

### Hints
*   How do you write a method that belongs to the class itself, not an object?
*   How do you write a helper function inside a class that doesn't need `cls` or `self`?
*   What determines exactly when `__del__` is called?
*   For Singleton: `__new__` allocates memory. If you store the instance on the class (e.g., `_instance`), you can return it if it already exists.

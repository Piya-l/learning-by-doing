# Task: Time Class Magic Methods

In this assignment, you will create a class to manage time (Hours, Minutes, Seconds). You will implement "Magic Methods" to allow adding and subtracting time objects naturally.

## Files to Create

1.  `my_time.py`: Contains your `Time` class.
2.  `main.py`: Contains the code to test your class.

## Instructions

### 1. Implement `Time` class in `my_time.py`

Your `Time` class must behave as follows:

**Constraints & Type Checking:**
*   For `__add__` and `__sub__`, you **MUST** check if the `other` operand is an instance of `Time`.
*   If it is NOT a `Time` object, you must raise a `TypeError` with the exact message: `"Operand must be a Time object"`.
*   For `__eq__`, if `other` is not a `Time` object, return `False`.

*   **`__init__(self, hour, minute, second)`**:
    *   Initialize the time.
    *   **CRITICAL REQUIREMENT**: You must automatically simplify the time.
        *   Example: `65 seconds` should convert to `1 minute, 5 seconds`.
        *   Example: `Time(2, 65, 0)` should become `03:05:00`.
        *   This ensures `str` output is always standardized (seconds < 60, minutes < 60).

*   **`__str__(self)`**:
    *   Return a string in the format `HH:MM:SS`.
    *   You **MUST** use zero-padding (e.g., `09:05:01`, not `9:5:1`).
    *   Hint: Use f-string formatting like `{self.hour:02d}`.

*   **`__add__(self, other)`**:
    *   Implement addition using `+`.
    *   Return a **new** `Time` object representing the total duration.
    *   Example: `01:30:00 + 00:45:00 = 02:15:00`.

*   **`__sub__(self, other)`**:
    *   Implement subtraction using `-`.
    *   Return a **new** `Time` object representing the difference.
    *   We assume we are measuring the "difference" or "duration" between two times, so the result should always be **positive**.
        *   Hint: Convert both times to total seconds, subtract, take the absolute value, and convert back to (h, m, s).

*   **`__eq__(self, other)`**:
    *   Return `True` if the total time is the same, `False` otherwise.

---

### 2. Verify with `main.py`

Since there is no automated checker for this assignment, you must verify your code manually.
Copy the following code into your `main.py` and run it.

```python
from my_time import Time

# 1. Create Time objects (Testing simplification)
t1 = Time(9, 30, 0)
t2 = Time(0, 80, 0) # Should simplify to 01:20:00

print(f"t1 = {t1}")
print(f"t2 = {t2}")

# 2. Check Addition
t3 = t1 + t2
print(f"t1 + t2 = {t3}")

# 3. Check Subtraction
t4 = t1 - t2
print(f"t1 - t2 = {t4}")

# 4. Check Equality
t5 = Time(10, 50, 0)
print(f"t3 == t5 is {t3 == t5}")
print(f"t3 == 'not a time' is {t3 == 'not a time'}")

# 5. Check Type Error messages
try:
    t1 + 10
except TypeError as e:
    print(f"t1 + 10 raised: {e}")

try:
    t1 - "hello"
except TypeError as e:
    print(f"t1 - 'hello' raised: {e}")
```

### Expected Output

If your class is correct, your output **must** match this exactly:

```text
t1 = 09:30:00
t2 = 01:20:00
t1 + t2 = 10:50:00
t1 - t2 = 08:10:00
t3 == t5 is True
t3 == 'not a time' is False
t1 + 10 raised: Operand must be a Time object
t1 - 'hello' raised: Operand must be a Time object
```

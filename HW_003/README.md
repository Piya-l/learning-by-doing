# Task: Magic Methods

In this assignment, you will explore Python's "Magic Methods" (Dunder methods) to customize the behavior of a class.

## Instructions

### 1. Create `coordinate.py`

Create a file named `coordinate.py` and implement a class named `Coordinate` representing a point in 4D space (x, y, z, w).

**Requirements:**

*   **Constraints**: You are **NOT** allowed to use any external libraries other than `math`.
*   **Type Checking**: For `__add__`, `__sub__`, and `__eq__`, you must check if the `other` operand is an instance of `Coordinate`. If it is not, verify that it raises a `TypeError` (except for `__eq__` where it should return `False`).

*   **`__init__(self, x, y, z, w)`**: Initialize the coordinate with `x`, `y`, `z`, and `w` values.
*   **`__str__(self)`**: Return a string representation in the format `<Coordinate is x, y, z, w>`.
*   **`__add__(self, other)`**: Implement addition using the `+` operator.
    *   Check if `other` is a `Coordinate` instance using `isinstance()`. If not, raise a `TypeError` with message "Operand must be a Coordinate".
    *   Return a **new** `Coordinate` instance where each value is the sum of the corresponding values.
*   **`__sub__(self, other)`**: Implement subtraction using the `-` operator.
    *   Check if `other` is a `Coordinate` instance using `isinstance()`. If not, raise a `TypeError` with message "Operand must be a Coordinate".
    *   Calculates the **Euclidean distance** ($\sqrt{(x_1-x_2)^2 + ...}$). Return a **float**.
*   **`__eq__(self, other)`**: Implement equality comparison.
    *   Check if `other` is a `Coordinate` instance. If not, return `False`.
    *   Two coordinates are equal if **all** their values are identical.

### 2. Create `main.py`

Create a file named `main.py` to test your class. It should perform the following actions and print the results exactly as shown below:

1.  Create `c1` (Point 1) with x=2, y=3, z=4, w=5.
2.  Create `c2` (Point 2) with x=5, y=7, z=9, w=11.
3.  Add `c1` and `c2` to get `c3` (New Point after move).
4.  Subtract `c2` from `c1` to get `distance`.
5.  Print the coordinates and the results. (Distance should be formatted to 4 decimal places implied by the output, or just print the standard float repr if simple). *Note: The example output shows approx values.*
6.  Check equality between `c1` and a new `Coordinate(2, 3, 4, 5)`.
7.  Check equality between `c1` and `c2`.

**Expected Output:**

```text
c1 = <Coordinate is 2, 3, 4, 5>
c2 = <Coordinate is 5, 7, 9, 11>
c3 = c1 + c2 = <Coordinate is 7, 10, 13, 16>
distance = c1 - c2 = 8.774964387392123
c1 == Coordinate(2, 3, 4, 5) is True
c1 == c2 is False
```

### 3. Verify

Run the provided test script to verify your implementation:

```sh
python chk_testcases.py
```

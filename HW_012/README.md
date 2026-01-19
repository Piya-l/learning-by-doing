# Homework 12: Product Inventory System

Implement a `Product` class with magic methods for comparisons, operators, and string representation.

## Requirements

### Class: `Product`

**Private Attributes** (`__`):
- `__name` - product name
- `__price` - price per unit
- `__quantity` - stock quantity

### Instance Methods

**`__init__(name, price, quantity=0)`**
- Initialize product with name, price, and quantity

**`restock(amount)`**
- Add to `__quantity`

**`sell(amount)`**
- Reduce `__quantity` if enough stock
- Return `True` if successful, `False` if not enough stock

**Accessor Methods:**
- `get_name()` - return name
- `get_price()` - return price
- `get_quantity()` - return quantity
- `get_value()` - return `price * quantity` (total inventory value)

### Magic Methods (Required)

**String Representation:**
- `__str__(self)` - Return: `"Product: [name], Price: $[price], Stock: [quantity]"`
- `__repr__(self)` - Return: `"Product('[name]', [price], [quantity])"`

**Comparison Operators** (compare by price):
- `__eq__(self, other)` - Equal if same price
- `__lt__(self, other)` - Less than if price lower
- `__le__(self, other)` - Less than or equal
- `__gt__(self, other)` - Greater than if price higher
- `__ge__(self, other)` - Greater than or equal

**Arithmetic Operators:**
- `__add__(self, other)` - Combine quantities, keep first product's name/price
  - Example: `p1 + p2` creates new Product with `p1.name`, `p1.price`, `p1.quantity + p2.quantity`
- `__mul__(self, number)` - Multiply quantity by number
  - Example: `p1 * 3` creates new Product with same name/price, quantity tripled

**Container Protocol:**
- `__len__(self)` - Return quantity (so `len(product)` works)
- `__bool__(self)` - Return `True` if quantity > 0, else `False`

## Magic Methods Summary

| Method | Purpose | Example |
|--------|---------|---------|
| `__str__` | Human-readable string | `print(p)` |
| `__repr__` | Developer string | `repr(p)` |
| `__eq__` | Equality comparison | `p1 == p2` |
| `__lt__` | Less than | `p1 < p2` |
| `__gt__` | Greater than | `p1 > p2` |
| `__add__` | Addition | `p1 + p2` |
| `__mul__` | Multiplication | `p * 3` |
| `__len__` | Length/count | `len(p)` |
| `__bool__` | Truthiness | `if p:` |

## Expected Output

When running `chk_homework.py`, you should see:

```
=== Testing Instance Creation ===
Created 3 products

=== Testing String Representations ===
str(p1): Product: Laptop, Price: $999.99, Stock: 10
repr(p1): Product('Laptop', 999.99, 10)
PASS: String representations

=== Testing Accessor Methods ===
Value of Laptop: $9999.9

=== Testing Comparison Operators ===
PASS: Comparison operators work correctly

=== Testing Arithmetic Operators ===
p1 + p4 = Laptop, quantity: 15
p2 * 3 = Mouse, quantity: 150

=== Testing Container Protocol ===
len(p1) = 10
bool(p1) = True (has stock)
bool(p3) = False (no stock)

=== Testing Restock and Sell ===
After restock +5: 15
PASS: Cannot sell more than stock
After sell 10: 5

=== Testing Access Control ===
PASS: Private attributes properly encapsulated

=== All Tests Passed ===
```

## Testing

Run `chk_homework.py` to verify all magic methods.

## Submission

Submit `homework.py` via GitHub Classroom.

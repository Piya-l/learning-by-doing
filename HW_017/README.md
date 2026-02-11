# Homework 17: Payment Gateway Adapter (Adapter Pattern)

Implement the **Adapter Design Pattern** to bridge a modern payment interface with a legacy vendor API.

## Learning Goals

- Understand the Adapter Pattern (Target, Client, Adaptee, and Adapter)
- Learn how to wrap a legacy interface to match a required target interface
- Practice unit conversion and method translation within an adapter

## Requirements

### Target Interface: `ModernPayment` (Goal)
The interface your application expects.
- `pay(amount_dollars)`: Accepts a float (e.g., 10.50).

### Adaptee: `OldVendorAPI` (Legacy)
A third-party library you cannot modify.
- `send_payment(amount_cents)`: Accepts an integer representing total cents (e.g., 1050).

### Adapter: `PaymentAdapter` (Your Task)
Connects the two.

**Protected Attributes** (`_`):
- `_legacy_api`: Instance of `OldVendorAPI`.

**Public Methods**:
- `__init__(legacy_api)`: Takes an instance of `OldVendorAPI`.
- `pay(amount_dollars)`: 
    1. Converts dollars to cents.
    2. Calls `legacy_api.send_payment()`.
    3. Returns the result from the legacy API.

## Access Level Summary

| Attribute/Method | Type | Access |
|-----------------|------|--------|
| `_legacy_api` | Protected | Internal/Subclasses |
| `pay()` | Public | Modern interface |
| `send_payment()` | Public | Legacy API |

## Expected Output

When running `chk_homework.py`, you should see:

```
=== Testing Adapter Pattern ===
PASS: Payment converted correctly (10.50 dollars -> 1050 cents)
PASS: Payment converted correctly (0.01 dollars -> 1 cent)
PASS: Adapter correctly implements ModernPayment interface

=== Testing with Real Example ===
Processing $19.99 through PaymentAdapter...
Old API received payment: 1999 cents. Success!

=== All Tests Passed ===
```

## Testing

Run `chk_homework.py` to verify your implementation.

## Submission

Submit `homework.py` via GitHub Classroom.

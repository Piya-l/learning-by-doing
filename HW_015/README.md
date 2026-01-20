# Homework 15: Bank Account Manager

Implement a `BankAccount` class demonstrating instance, static, and class methods with proper access control.

## Requirements

### Class: `BankAccount`

**Private Attributes** (`__`):
- `__account_number` - unique account ID
- `__balance` - current balance
- `__pin` - 4-digit PIN

**Protected Attributes** (`_`):
- `_account_type` - "Savings" or "Checking"

**Class Attributes**:
- `_total_accounts` - count of all accounts created
- `_bank_name` - name of the bank (default: "PyBank")

### Instance Methods

**`__init__(account_number, pin, account_type="Savings")`**
- Validate PIN is 4 digits, raise `ValueError` if not
- Initialize balance to 0
- Increment `_total_accounts`

**`deposit(amount)`**
- Add amount to balance
- Return new balance

**`withdraw(amount, pin)`**
- Check PIN matches, return `False` if wrong
- Check sufficient balance, return `False` if not enough
- Deduct amount and return `True` if successful

**`get_balance(pin)`**
- Return balance if PIN correct, else return `None`

**`get_account_number()`**
- Return account number

### Static Methods

**`@staticmethod validate_pin(pin)`**
- Return `True` if pin is 4-digit string, else `False`
- Should work without creating instance: `BankAccount.validate_pin("1234")`

**`@staticmethod calculate_interest(balance, rate)`**
- Return `balance * rate`
- Utility function, no access to instance/class

### Class Methods

**`@classmethod get_total_accounts(cls)`**
- Return `_total_accounts`

**`@classmethod set_bank_name(cls, name)`**
- Set `_bank_name` for all accounts

**`@classmethod get_bank_name(cls)`**
- Return `_bank_name`

## Access Level Summary

| Attribute/Method | Type | Access |
|-----------------|------|--------|
| `__account_number`, `__balance`, `__pin` | Private | Internal only |
| `_account_type` | Protected | Subclasses |
| `_total_accounts`, `_bank_name` | Class | Shared across all instances |
| `deposit()`, `withdraw()`, `get_balance()` | Instance | Needs `self` |
| `validate_pin()`, `calculate_interest()` | Static | No `self` or `cls` |
| `get_total_accounts()`, `set_bank_name()` | Class | Needs `cls` |

## Expected Output

When running `chk_homework.py`, you should see:

```
=== Testing Static Methods ===
PASS: validate_pin() works
PASS: calculate_interest() works

=== Testing Class Methods ===
Initial accounts: 0
Bank name: TestBank

=== Testing Instance Creation ===
PASS: Rejected invalid PIN
Created 2 accounts
Total accounts: 2 (expected 2)

=== Testing Instance Methods ===
Account number: ACC001
After deposit $1000: $1000
PASS: Wrong PIN rejected
Balance with correct PIN: $1000
PASS: Wrong PIN withdrawal rejected
PASS: Insufficient funds withdrawal rejected
After $300 withdrawal: $700

=== Testing Access Control ===
PASS: Private attributes properly encapsulated

=== All Tests Passed ===
```

## Testing

Run `chk_homework.py` to verify implementation.

## Submission

Submit `homework.py` via GitHub Classroom.

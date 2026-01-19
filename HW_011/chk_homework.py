"""
Test file for HW_011: Bank Account Manager
"""

from homework import BankAccount

def test_bank_account():
    print("=== Testing Static Methods ===")
    # Test without creating instance
    assert BankAccount.validate_pin("1234") == True, "FAIL: Valid PIN"
    assert BankAccount.validate_pin("123") == False, "FAIL: Short PIN"
    assert BankAccount.validate_pin("12345") == False, "FAIL: Long PIN"
    assert BankAccount.validate_pin("abcd") == False, "FAIL: Non-digit PIN"
    print("PASS: validate_pin() works")
    
    # Test interest calculation
    assert BankAccount.calculate_interest(1000, 0.05) == 50.0, "FAIL: Interest calc"
    print("PASS: calculate_interest() works")
    
    print("\n=== Testing Class Methods ===")
    initial_count = BankAccount.get_total_accounts()
    print(f"Initial accounts: {initial_count}")
    
    BankAccount.set_bank_name("TestBank")
    assert BankAccount.get_bank_name() == "TestBank", "FAIL: Bank name"
    print(f"Bank name: {BankAccount.get_bank_name()}")
    
    print("\n=== Testing Instance Creation ===")
    try:
        acc1 = BankAccount("ACC001", "123", "Savings")  # Invalid PIN
        print("FAIL: Should reject short PIN")
    except ValueError:
        print("PASS: Rejected invalid PIN")
    
    acc1 = BankAccount("ACC001", "1234", "Savings")
    acc2 = BankAccount("ACC002", "5678", "Checking")
    print(f"Created 2 accounts")
    print(f"Total accounts: {BankAccount.get_total_accounts()} (expected {initial_count + 2})")
    
    print("\n=== Testing Instance Methods ===")
    assert acc1.get_account_number() == "ACC001", "FAIL: Account number"
    print(f"Account number: {acc1.get_account_number()}")
    
    # Test deposit
    new_balance = acc1.deposit(1000)
    assert new_balance == 1000, "FAIL: Deposit"
    print(f"After deposit $1000: ${new_balance}")
    
    # Test balance check with wrong PIN
    assert acc1.get_balance("0000") is None, "FAIL: Wrong PIN should return None"
    print("PASS: Wrong PIN rejected")
    
    # Test balance check with correct PIN
    assert acc1.get_balance("1234") == 1000, "FAIL: Correct balance"
    print(f"Balance with correct PIN: ${acc1.get_balance('1234')}")
    
    # Test withdrawal with wrong PIN
    result = acc1.withdraw(100, "0000")
    assert result == False, "FAIL: Wrong PIN withdrawal"
    print("PASS: Wrong PIN withdrawal rejected")
    
    # Test withdrawal with insufficient funds
    result = acc1.withdraw(2000, "1234")
    assert result == False, "FAIL: Insufficient funds"
    print("PASS: Insufficient funds withdrawal rejected")
    
    # Test successful withdrawal
    result = acc1.withdraw(300, "1234")
    assert result == True, "FAIL: Withdrawal"
    assert acc1.get_balance("1234") == 700, "FAIL: Balance after withdrawal"
    print(f"After $300 withdrawal: ${acc1.get_balance('1234')}")
    
    print("\n=== Testing Access Control ===")
    # Check private attributes are not accessible
    has_public_attrs = hasattr(acc1, 'balance') or hasattr(acc1, 'pin') or hasattr(acc1, 'account_number')
    if has_public_attrs:
        print("FAIL: Private attributes should not be public")
    else:
        print("PASS: Private attributes properly encapsulated")
    
    print("\n=== All Tests Passed ===")

if __name__ == "__main__":
    test_bank_account()

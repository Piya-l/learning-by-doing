from homework import BankAccount

print("=== 1. Testing Transactions ===")
acc = BankAccount("001", "8888")
print(f"Account: {acc.get_account_number()}")

# Deposit
bal = acc.deposit(500)
print(f"Deposited $500. Balance: {bal}")

# Withdraw success
ok = acc.withdraw(200, "8888")
print(f"Withdraw $200 (PIN 8888): {ok}")
print(f"Balance check (PIN 8888): {acc.get_balance('8888')}")

# Withdraw fail (pin)
ok = acc.withdraw(100, "0000")
print(f"Withdraw $100 (PIN 0000): {ok}")

# Withdraw fail (balance)
ok = acc.withdraw(1000, "8888")
print(f"Withdraw $1000 (PIN 8888): {ok}")

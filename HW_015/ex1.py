from homework import BankAccount

print("=== 1. Testing Class & Static Methods ===")
print(f"Initial accounts: {BankAccount.get_total_accounts()}")
print(f"Valid PIN '1234': {BankAccount.validate_pin('1234')}")
print(f"Valid PIN '12': {BankAccount.validate_pin('12')}")
print(f"Interest on $1000 at 5%: ${BankAccount.calculate_interest(1000, 0.05)}")

print("\n=== 2. Creating Accounts ===")
a1 = BankAccount("001", "1234", "Savings")
a2 = BankAccount("002", "5678", "Checking")
print(f"Total accounts now: {BankAccount.get_total_accounts()}")

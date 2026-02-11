from homework import PaymentAdapter, OldVendorAPI

# Represents a list of transaction objects
transactions = [
    {"user": "Alice", "amount": 10.00},
    {"user": "Bob", "amount": 25.50},
    {"user": "Charlie", "amount": 5.75}
]

# Legacy system
bank_v1 = OldVendorAPI()
adapter = PaymentAdapter(bank_v1)

print("=== Batch Processing Transactions ===")
for tx in transactions:
    print(f"Processing for {tx['user']}: ${tx['amount']}")
    # The adapter handles the translation for each object
    adapter.pay(tx['amount'])
    print("-" * 20)

print("Batch Processing Finished.")

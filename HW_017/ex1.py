from homework import PaymentAdapter, OldVendorAPI

# 1. Setup the legacy system
legacy_system = OldVendorAPI()

# 2. Use the Adapter to make it compatible with our modern expectations
payment_processor = PaymentAdapter(legacy_system)

# 3. Pay in dollars as if we are using a modern API
amount = 49.95
print(f"Customer is paying ${amount}...")
payment_processor.pay(amount)

print("Payment processing complete.")

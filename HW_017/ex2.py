from homework import PaymentAdapter, OldVendorAPI, ModernPayment

# A client class that only knows about the ModernPayment interface
class ShoppingCart:
    def __init__(self, payment_processor: ModernPayment):
        self.processor = payment_processor
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))
        print(f"Added {name} for ${price}")

    def checkout(self):
        total = sum(item[1] for item in self.items)
        print(f"\nFinal Total: ${total:.2f}")
        print("Processing payment...")
        self.processor.pay(total)
        print("Checkout Complete.")

# --- Test Case 1: Using the Adapter ---
print("--- Using Video Game Store (Legacy Backend) ---")
legacy_api = OldVendorAPI()
adapter = PaymentAdapter(legacy_api)

cart = ShoppingCart(adapter)
cart.add_item("Cyberpunk 2077", 29.99)
cart.add_item("Elden Ring", 59.99)
cart.checkout()

# --- Test Case 2: Using a Native Modern Implementation ---
# (Usually defined in your app, not the adapter library)
class StripeGateway(ModernPayment):
    def pay(self, amount_dollars):
        print(f"Stripe processed ${amount_dollars} directly.")
        return True

print("\n--- Using Clothing Store (Modern Backend) ---")
modern_api = StripeGateway()
cart2 = ShoppingCart(modern_api)
cart2.add_item("Cool Shirt", 15.00)
cart2.checkout()

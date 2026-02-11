# This represents the Adaptee (Legacy)
class OldVendorAPI:
    def send_payment(self, amount_cents):
        print(f"Old API received payment: {amount_cents} cents. Success!")
        return True

# This represents the Target Interface
class ModernPayment:
    def pay(self, amount_dollars):
        raise NotImplementedError("Subclasses must implement pay()")

# Your Task: Implement the Adapter
class PaymentAdapter(ModernPayment):
    def __init__(self, legacy_api):
        # TODO: Store the legacy_api instance as a protected attribute _legacy_api
        pass

    def pay(self, amount_dollars):
        # TODO: 
        # 1. Convert amount_dollars to cents (int)
        # 2. Call self._legacy_api.send_payment()
        # 3. Return the result
        pass

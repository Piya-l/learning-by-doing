from homework import PaymentAdapter, ModernPayment

# Mock legacy API for testing
class MockOldAPI:
    def __init__(self):
        self.last_amount = None
    
    def send_payment(self, amount_cents):
        self.last_amount = amount_cents
        return "OK"

def test_adapter():
    print("=== Testing Adapter Pattern ===")
    mock_api = MockOldAPI()
    adapter = PaymentAdapter(mock_api)
    
    # Test 1: Basic conversion
    res = adapter.pay(10.50)
    assert mock_api.last_amount == 1050, f"FAIL: Expected 1050 cents, got {mock_api.last_amount}"
    print("PASS: Payment converted correctly (10.50 dollars -> 1050 cents)")
    
    # Test 2: Edge case (small amount)
    adapter.pay(0.01)
    assert mock_api.last_amount == 1, f"FAIL: Expected 1 cent, got {mock_api.last_amount}"
    print("PASS: Payment converted correctly (0.01 dollars -> 1 cent)")
    
    # Test 3: Inheritance check
    assert isinstance(adapter, ModernPayment), "FAIL: Adapter should inherit from ModernPayment"
    print("PASS: Adapter correctly implements ModernPayment interface")

    print("\n=== Testing with Real Example ===")
    from homework import OldVendorAPI
    real_legacy = OldVendorAPI()
    real_adapter = PaymentAdapter(real_legacy)
    print("Processing $19.99 through PaymentAdapter...")
    real_adapter.pay(19.99)

    print("\n=== All Tests Passed ===")

if __name__ == "__main__":
    test_adapter()

"""
Test file for HW_012: Product Inventory System
"""

from homework import Product

def test_product():
    print("=== Testing Instance Creation ===")
    p1 = Product("Laptop", 999.99, 10)
    p2 = Product("Mouse", 25.50, 50)
    p3 = Product("Keyboard", 75.00, 0)
    print(f"Created 3 products")
    
    print("\n=== Testing String Representations ===")
    print(f"str(p1): {str(p1)}")
    print(f"repr(p1): {repr(p1)}")
    assert "Laptop" in str(p1), "FAIL: __str__"
    assert "999.99" in str(p1), "FAIL: __str__ price"
    assert "Product(" in repr(p1), "FAIL: __repr__"
    print("PASS: String representations")
    
    print("\n=== Testing Accessor Methods ===")
    assert p1.get_name() == "Laptop", "FAIL: get_name"
    assert p1.get_price() == 999.99, "FAIL: get_price"
    assert p1.get_quantity() == 10, "FAIL: get_quantity"
    assert p1.get_value() == 9999.90, "FAIL: get_value"
    print(f"Value of {p1.get_name()}: ${p1.get_value()}")
    
    print("\n=== Testing Comparison Operators ===")
    # Compare by price
    assert p1 > p2, "FAIL: p1 should be > p2"
    assert p2 < p1, "FAIL: p2 should be < p1"
    assert p2 <= p1, "FAIL: p2 should be <= p1"
    assert p1 >= p2, "FAIL: p1 should be >= p2"
    p4 = Product("Desktop", 999.99, 5)
    assert p1 == p4, "FAIL: p1 should == p4 (same price)"
    print("PASS: Comparison operators work correctly")
    
    print("\n=== Testing Arithmetic Operators ===")
    # Test addition (combines quantities)
    p5 = p1 + p4
    assert p5.get_name() == "Laptop", "FAIL: __add__ name"
    assert p5.get_price() == 999.99, "FAIL: __add__ price"
    assert p5.get_quantity() == 15, "FAIL: __add__ quantity"
    print(f"p1 + p4 = {p5.get_name()}, quantity: {p5.get_quantity()}")
    
    # Test multiplication
    p6 = p2 * 3
    assert p6.get_name() == "Mouse", "FAIL: __mul__ name"
    assert p6.get_price() == 25.50, "FAIL: __mul__ price"
    assert p6.get_quantity() == 150, "FAIL: __mul__ quantity"
    print(f"p2 * 3 = {p6.get_name()}, quantity: {p6.get_quantity()}")
    
    print("\n=== Testing Container Protocol ===")
    # Test __len__
    assert len(p1) == 10, "FAIL: __len__"
    print(f"len(p1) = {len(p1)}")
    
    # Test __bool__
    assert bool(p1) == True, "FAIL: __bool__ with stock"
    assert bool(p3) == False, "FAIL: __bool__ without stock"
    print(f"bool(p1) = {bool(p1)} (has stock)")
    print(f"bool(p3) = {bool(p3)} (no stock)")
    
    print("\n=== Testing Restock and Sell ===")
    p1.restock(5)
    assert p1.get_quantity() == 15, "FAIL: restock"
    print(f"After restock +5: {p1.get_quantity()}")
    
    result = p1.sell(20)
    assert result == False, "FAIL: sell too many"
    print("PASS: Cannot sell more than stock")
    
    result = p1.sell(10)
    assert result == True, "FAIL: sell"
    assert p1.get_quantity() == 5, "FAIL: sell quantity"
    print(f"After sell 10: {p1.get_quantity()}")
    
    print("\n=== Testing Access Control ===")
    has_public_attrs = hasattr(p1, 'name') or hasattr(p1, 'price') or hasattr(p1, 'quantity')
    if has_public_attrs:
        print("FAIL: Private attributes should not be public")
    else:
        print("PASS: Private attributes properly encapsulated")
    
    print("\n=== All Tests Passed ===")

if __name__ == "__main__":
    test_product()

from homework import SmartHome, Device

def test_iterator():
    print("=== Testing SmartHome Iterator ===")
    home = SmartHome()
    home.add_device(Device("Living Room Light", "Light"))
    home.add_device(Device("Kitchen Thermostat", "Thermostat"))
    home.add_device(Device("Front Door Camera", "Camera"))
    
    print(f"PASS: Created SmartHome with {len(home.devices)} devices")
    
    # Test iteration
    expected = ["Living Room Light (Light)", "Kitchen Thermostat (Thermostat)", "Front Door Camera (Camera)"]
    actual = []
    
    try:
        for device in home:
            actual.append(str(device))
        
        assert actual == expected, f"FAIL: Expected {expected}, got {actual}"
        print("PASS: Successfully iterated through all devices")
        
        # Test iterator exhaustion
        it = iter(home)
        for _ in range(3):
            next(it)
        
        try:
            next(it)
            print("FAIL: Iterator should have raised StopIteration")
        except StopIteration:
            print("PASS: Iterator raised StopIteration at the end")
            
    except Exception as e:
        print(f"FAIL: Iterator logic error: {e}")
        return

    print("\n=== Testing Multiple Iterators ===")
    it1 = iter(home)
    it2 = iter(home)
    
    d1 = next(it1)
    d2 = next(it2)
    
    assert str(d1) == str(d2) == "Living Room Light (Light)", "FAIL: Independent iterators"
    next(it1)
    d1_second = next(it1)
    assert str(d1_second) == "Front Door Camera (Camera)", "FAIL: it1 should be at 3rd element"
    assert str(next(it2)) == "Kitchen Thermostat (Thermostat)", "FAIL: it2 should be at 2nd element"
    print("PASS: Two independent iterators working correctly")

    print("\n=== All Tests Passed ===")

if __name__ == "__main__":
    test_iterator()

from homework import Droid, ProtocolDroid, FactoryAI
import time

def test_droid_factory():
    print("=== 1. Testing Static & Class Methods ===")
    try:
        # Static Method Check
        if hasattr(Droid, 'verify_serial_code'):
            if Droid.verify_serial_code("AZ-1001") == True and Droid.verify_serial_code("wrong") == False:
                 print("PASS: verify_serial_code works.")
            else:
                 print("FAIL: verify_serial_code logic seems wrong.")
        else:
             print("FAIL: verify_serial_code method missing.")
             
        # Class Method Check (Population)
        initial_pop = Droid.get_population()
        print(f"Initial Population: {initial_pop}")
        
    except Exception as e:
        print(f"Error in Static/Class method test: {e}")

    print("\n=== 2. Testing Creation & Validation ===")
    try:
        try:
            d1 = Droid("R2", "invalid_serial")
            print("FAIL: Should have raised ValueError for invalid serial.")
        except ValueError:
            print("PASS: correctly rejected invalid serial.")
            
        d2 = Droid("Alpha", "AZ-0001")
        d3 = Droid("Beta", "AZ-0002")
        print(f"Created: {d2}")
        print(f"Created: {d3}")
        
        current_pop = Droid.get_population()
        print(f"Current Population: {current_pop} (Expected {initial_pop + 2 if 'initial_pop' in locals() else 'unknown'})")

    except Exception as e:
        print(f"Error in Creation test: {e}")

    print("\n=== 3. Testing Magic Methods (Comparisons & Operators) ===")
    try:
        # Power levels default 50
        if d2 == d3:
            print("FAIL: d2 and d3 have different serials.")
        else:
            print("PASS: d2 != d3")
            
        # Manually hacking power for test (student code handles attributes)
        # We assume attributes are accessible or use getters if specified, but spec implies typical attribute usage or no strict privacy on power
        # Spec says: Sets power_level to 50.
        # Let's try to set it if possible, or creates new ones.
        
        # d2 > d3 ? Both 50.
        if d2 > d3:
             print("FAIL: 50 is not > 50")
        else:
             print("PASS: 50 is not > 50")

        # Fusion
        # d4 = d2 + d3
        # Name: Alpha-Beta
        # Serial: AZ-0001-AZ-0002
        # Power: 100
        d4 = d2 + d3 
        print(f"Fused Droid: {d4}")
        
        if d4 > d2:
             print("PASS: Fusion droid is stronger.")
        else:
             print("FAIL: Fusion droid should be stronger.")

    except Exception as e:
        print(f"Error in Magic Method test: {e}")

    print("\n=== 4. Testing Inheritance & Access ===")
    try:
        p1 = ProtocolDroid("C-3PO", "AZ-9999", ["English", "Bocce"])
        print(p1)
        
        p1.translate("Hello")
        p1.translate("Hola", "English")
        p1.translate("Bleep", "Sith")
        
    except Exception as e:
        print(f"Error in Subclass test: {e}")

    print("\n=== 5. Testing Destruction (Simulated) ===")
    try:
        # Note: __del__ is tricky to test deterministically.
        # We will just delete reference and hope it prints.
        print("Deleting d2...")
        del d2
        # Force garbage collection might be needed in real env, but for simple script usually works.
        import gc
        gc.collect() 
        
        pop_after = Droid.get_population()
        print(f"Population after delete: {pop_after}")
        
    except Exception as e:
        print(f"Error in Destruction test: {e}")

    print("\n=== 6. Testing Singleton (FactoryAI) ===")
    try:
        ai1 = FactoryAI()
        ai1.authorize_production()
        
        ai2 = FactoryAI()
        if ai1 is ai2:
            print("PASS: ai1 and ai2 are the SAME object.")
        else:
            print("FAIL: ai1 and ai2 are DIFFERENT objects. Singleton failed.")
            
    except Exception as e:
        print(f"Error in Singleton test: {e}")

if __name__ == "__main__":
    test_droid_factory()

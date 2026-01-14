from homework import Employee, Manager, Developer

def test_homework():
    print("--- Testing Employee ---")
    try:
        emp = Employee("Alice", 50000)
        print(emp.get_details())
        emp.work("Reporting")
        emp.work("Analysis", 3)
    except Exception as e:
        print(f"Error testing Employee: {e}")

    print("\n--- Testing Manager ---")
    try:
        mgr = Manager("Bob", 90000, "Sales")
        print(mgr.get_details())
        mgr.work("Meeting")
    except Exception as e:
        print(f"Error testing Manager: {e}")

    print("\n--- Testing Developer ---")
    try:
        dev = Developer("Charlie", 80000, "Python")
        print(dev.get_details())
        dev.work("Coding")
    except Exception as e:
        print(f"Error testing Developer: {e}")

if __name__ == "__main__":
    test_homework()

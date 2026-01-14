from homework import Manager, Developer

print("--- Testing Manager ---")
mgr = Manager("Bob", 90000, "Sales")
print(mgr.get_details())
mgr.work("Meeting")

print("\n--- Testing Developer ---")
dev = Developer("Charlie", 80000, "Python")
print(dev.get_details())
dev.work("Coding")

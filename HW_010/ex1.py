from homework import Droid

print("=== 1. Testing Creation & Validation ===")
d1 = Droid("Alpha", "AZ-0001")
d2 = Droid("Beta", "AZ-0002")
print(f"Created: {d1}")
print(f"Created: {d2}")

print(f"Current Population: {Droid.get_population()}")

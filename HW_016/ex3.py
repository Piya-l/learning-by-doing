from homework import SmartHome, Device

# Setup
home = SmartHome()
home.add_device(Device("Smart Light", "Light"))
home.add_device(Device("Smart Lock", "Security"))

print("=== First Loop ===")
for device in home:
    print(f"Loop 1: {device}")

print("\n=== Second Loop (Consecutive) ===")
# Testing if the collection can be iterated again
# This works because __iter__ returns a NEW iterator instance each time
for device in home:
    print(f"Loop 2: {device}")

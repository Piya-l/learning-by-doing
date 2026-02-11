from homework import SmartHome, Device

# Setup
home = SmartHome()
home.add_device(Device("WiFi Router", "Network"))
home.add_device(Device("Smart Speaker", "Audio"))

print("=== Demonstration 1: Manual next() ===")
it = iter(home)
# Manually getting elements
first = next(it)
print(f"First device: {first}")

second = next(it)
print(f"Second device: {second}")

try:
    third = next(it)
except StopIteration:
    print("No more devices (StopIteration raised)")

print("\n=== Demonstration 2: While loop with next() ===")
# This is what a 'for' loop does under the hood
it2 = iter(home)
while True:
    try:
        device = next(it2)
        print(f"Device: {device}")
    except StopIteration:
        print("End of list reached.")
        break

from homework import SmartHome, Device

# Create a Smart Home collection
my_home = SmartHome()

# Add some devices
my_home.add_device(Device("Smart TV", "Entertainment"))
my_home.add_device(Device("AC Unit", "Appliance"))
my_home.add_device(Device("Main Gate", "Security"))

print("Listing all devices in my smart home:")
print("-" * 30)

# Use the iterator pattern in a for loop
for device in my_home:
    print(f"- {device}")

print("-" * 30)
print("Done!")

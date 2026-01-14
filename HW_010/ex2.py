from homework import Droid, ProtocolDroid

print("=== Testing Magic Methods ===")
d1 = Droid("Alpha", "AZ-0001")
d2 = Droid("Beta", "AZ-0002")
d3 = d1 + d2
print(f"Fused Droid: {d3}")

print("\n=== Testing Inheritance ===")
p1 = ProtocolDroid("C-3PO", "AZ-9999", ["English", "Bocce"])
print(p1)
p1.translate("Hello")
p1.translate("Hola", "English")

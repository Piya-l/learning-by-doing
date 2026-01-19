from homework import Product

print("=== 1. Creation & String Repr ===")
p1 = Product("Apple", 1.5, 100)
p2 = Product("Banana", 0.8, 50)
print(p1)
print(repr(p2))

print("\n=== 2. Comparison (by Price) ===")
print(f"Apple($1.5) > Banana($0.8): {p1 > p2}")
print(f"Apple($1.5) == Banana($0.8): {p1 == p2}")

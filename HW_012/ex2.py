from homework import Product

print("=== 1. Arithmetic Operations ===")
p1 = Product("Apple", 1.5, 10)
p2 = Product("Green Apple", 1.5, 5)

# Addition
p3 = p1 + p2
print(f"Combined: {p3}")

# Multiplication
p4 = p1 * 2
print(f"Multiplied: {p4}")

print("\n=== 2. Stock Management ===")
print(f"Has stock? {bool(p1)}")
p1.sell(10)
print(f"Sold 10. Has stock? {bool(p1)}")
print(f"Stock count: {len(p1)}")

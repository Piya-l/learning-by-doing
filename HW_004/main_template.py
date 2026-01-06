from my_classes import Customer, CustomerLevel, Product, CashRegister, Report, LoadData

# Load data from CSV files
# TODO: Load customer_levels and products using LoadData class
# customer_levels = ...
# products = ...

# Example usage
# TODO: Initialize a Report instance
# session_report = ...

#Transaction 1
# Create an instance of CashRegister
# TODO: Create a temporary customer (Regular, John Doe) and cash register
# TODO: Load products into cash register
# TODO: Add products: SSWB002 (2), YM005 (5), FT009 (1), BS003 (1)
# TODO: Print summary total
# TODO: Add cash register to session_report

# Transactions data 2...n
transactions = [
    {
        "customer_level": "VIP",
        "customer_name": "Any Name",
        "products": [("YM005", 2), ("YM005", 5), ("NCH008", 1), ("ILB010", 1)],
    },
    {
        "customer_level": "Silver",
        "customer_name": "Alice Smith",
        "products": [("WE001", 2), ("LDL007", 1), ("SSWB002", 3)],
    },
    {
        "customer_level": "VIP",
        "customer_name": "Emily Davis",
        "products": [("NCH008", 2), ("YM005", 1), ("SS004", 3)],
    },
    # TODO: One transaction is missing here. Hint: See the expected output in chk_testcases.py to determine the missing transaction data (Customer: Charlie Brown).
]

# Process transactions
for transaction in transactions:
    # TODO: Create customer and cash register based on transaction data
    # TODO: Load products
    # TODO: Add products from the transaction["products"] list
    # TODO: Print summary total
    # TODO: Add to session_report
    pass

print()
print("...DONE TRANSACTION...")
print()

# Print summary report
# TODO: internalize session_report.summary_report()

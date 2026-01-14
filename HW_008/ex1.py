from homework import Employee

print("--- Testing Employee ---")
emp = Employee("Alice", 50000)
print(emp.get_details())
emp.work("Reporting")
emp.work("Analysis", 3)

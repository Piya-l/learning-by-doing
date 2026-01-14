from homework import Employee

print("--- Testing Lifecycle (Debug=True) ---")
emp = Employee("DebugEmp", 0, debug=True)
print("Working...")
emp.work("Testing")
del emp
print("Done.")

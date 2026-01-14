# Employee Management System

## Concepts Covered
- **Inheritance**: Creating subclasses that inherit properties and methods from a base class.
- **Method Overriding**: Redefining a method in a subclass to change its behavior.
- **Method Overloading (Simulation)**: Using default arguments to allow a method to be called with different numbers of parameters.

## Instructions

Create a file named `homework.py` and implement the following classes:

### 1. Class `Employee` (Base Class)
*   **Attributes**:
    *   `name`: (str) The name of the employee.
    *   `salary`: (float) The salary of the employee.
*   **Methods**:
    *   `__init__(self, name, salary)`: Initializes the attributes.
    *   `get_details(self)`: Returns a string in the format:  
        `"Name: {name}, Salary: {salary}"`
    *   `work(self, task_name, hours=None)`: **(Method Overloading Simulation)**
        *   If `hours` is NOT provided (None), print:  
            `"{name} is working on {task_name}."`
        *   If `hours` IS provided, print:  
            `"{name} is working on {task_name} for {hours} hours."`

### 2. Class `Manager` (Inherits from `Employee`)
*   **Attributes**:
    *   Inherits `name` and `salary`.
    *   Adds `department`: (str) The department the manager oversees.
*   **Methods**:
    *   `__init__(self, name, salary, department)`: Initializes all attributes (hint: use `super()`).
    *   `get_details(self)`: **(Method Overriding)**  
        Overrides the parent method to return:  
        `"Name: {name}, Salary: {salary}, Department: {department}"`

### 3. Class `Developer` (Inherits from `Employee`)
*   **Attributes**:
    *   Inherits `name` and `salary`.
    *   Adds `programming_language`: (str) The language the developer uses.
*   **Methods**:
    *   `__init__(self, name, salary, programming_language)`: Initializes all attributes.
    *   `get_details(self)`: **(Method Overriding)**  
        Overrides the parent method to return:  
        `"Name: {name}, Salary: {salary}, Language: {programming_language}"`

### 4. Lifecycle Debugging (New Requirement)
*   **Debug Flag**:
    *   All classes (`Employee`, `Manager`, `Developer`) must accept an optional keyword argument `debug` (default: `False`) in their `__init__` and object creation.
*   **Behavior**:
    *   If `debug` is `True`, the object must print messages during its lifecycle:
        1.  **Creation (`__new__`)**: Print `"[Class Name] loaded."`
        2.  **Initialization (`__init__`)**: Print `"[Class Name] initialized: [name]"`
        3.  **Destruction (`__del__`)**: Print `"[Class Name] [name] deleted."`
        4.  **Methods (`get_details`, `work`)**: Print `"[Class Name] method [method_name] called."` before performing the action.
*   **Implementation Note**:
    *   You will need to override `__new__`, `__init__`, and `__del__`.
    *   Ensure `debug` state is stored so `__del__` knows whether to print.
    *   All methods must check `self.debug` before execution.

---

## Testing Your Code

You can verify your implementation by running the provided `chk_homework.py` script:

```bash
python chk_homework.py
```

### Expected Output Example

```text
--- Testing Employee ---
Name: Alice, Salary: 50000
Alice is working on Reporting.
Alice is working on Analysis for 3 hours.

--- Testing Manager ---
Name: Bob, Salary: 90000, Department: Sales
Bob is working on Meeting.

--- Testing Developer ---
Name: Charlie, Salary: 80000, Language: Python
Charlie is working on Coding.

--- Testing Lifecycle (Debug=True) ---
Employee loaded.
Employee initialized: DebugEmp
Employee method work called.
DebugEmp is working on Testing.
Employee DebugEmp deleted.
```

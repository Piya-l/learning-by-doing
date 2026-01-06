# Task 2

You will be creating the `main.py` and `shape.py` files. Your task is to ensure that the script outputs the correct messages and handles input as specified.

## Instructions

1. **Create `main.py` and `shape.py`**
   - Ensure the following requirements are met:
     1. The `Shape` class can hold either a Triangle or a Rectangle.
     2. The `Shape` class contains three attributes: `shape_type`, `width`, and `height`. All variables must be private to prevent unintended modification (with `__` in front of their names).
     3. The `shape_type`, `width`, and `height` are used in the constructor of the class.
     4. The `Shape` class contains two methods: `print_info()` and `set_property(shape_type, width, height)`.
        - The `print_info()` method prints the shape type along with its width, height, and area.
        - The `set_property(shape_type, width, height)` method sets the properties of the shape with the given shape_type, width, and height.
     5. The program should follow the format exactly as provided in the examples.
     6. All number values are displayed with 1 digit after the decimal place.
     7. The test cases are provided in the file `testcases.txt`.



2. **Running the Script Normally:**
   - To run the script normally, open your terminal and navigate to the directory containing `main.py`.
   - Execute the script using Python:
     ```sh
     python main.py
     ```

3. **Running the Script with Test Cases:**
   - To check your script against the provided test cases, you can use the `chk_testcases.py` script.
   - Open your terminal and navigate to the directory containing `chk_testcases.py`.
   - Execute the test script using Python:
     ```sh
     python chk_testcases.py
     ```

## Output from the Unittest

Here is an example of what the output might look like when you run the test script:

>```
>..
>----------------------------------------------------------------------
>Ran 2 tests in 0.000s
>
>OK
>```


This output indicates that both test cases have passed successfully. If there are any issues with your script, the unittest framework will provide detailed information about the failures.

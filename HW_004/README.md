# Task

You will be creating/modifying the `main.py` and `my_classes.py` files. Your task is to ensure that the scripts are dynamic, output the correct messages, and handle input (transactions) as specified.

## Instructions

1.  **Setup your environment:**
    *   Rename `main_template.py` to `main.py`. This will be your main working file.
    *   Create a new file named `my_classes.py`.

2.  **Implement Classes:**
    *   In `my_classes.py`, implement the following classes based on their usage in `main.py`:
        *   `CustomerLevel`
        *   `Product`
        *   `Customer`
        *   `CashRegister`
        *   `Report`
        *   `LoadData`
    *   The csv files (`customer_levels.csv` and `products.csv`) are your data sources.
    *   **Note:** Your `my_classes.py` may be used in other environments (e.g., with a different `main.py` containing different transactions or different `.csv` database files). Ensure your code is dynamic and not hardcoded to specific data in the example.

3.  **Complete the Main Logic:**
    *   In `main.py`, fill in the TODO sections to implement the logic for processing transactions and generating the report.
    *   **CRITICAL STEP:** There is a missing transaction in the `transactions` list in `main.py` (marked with a TODO).
    *   Run the test checker to discover the missing transaction details.

4.  **Running the Script Normally:**
    *   To run the script normally, open your terminal and navigate to the directory containing `main.py`.
    *   Execute the script using Python:
        ```sh
        python main.py
        ```

5.  **Running the Script with Test Cases:**
    *   To check your script against the provided test cases, use the `chk_testcases.py` script.
    *   Test cases will help you find the missing transaction data (Look for "Charlie Brown").
    *   Execute the test script using Python:
        ```sh
        python chk_testcases.py
        ```

## Output from the Unittest

Here is an example of what the output might look like when you run the test script:

> ```
> .
> ----------------------------------------------------------------------
> Ran 1 test in 0.000s
>
> OK
> ```

This output indicates that the test case has passed successfully. If there are any issues (like the missing transaction), the unittest framework will show you the difference between your output and the expected output. Use that difference to fix your code!
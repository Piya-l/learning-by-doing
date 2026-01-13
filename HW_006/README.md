# MyDate Class Assignment

The `MyDate` class models a date instance and includes methods for validating and manipulating dates. Below are the details of the class requirements.

> **Note**: You are **not allowed** to use any Date libraries in this implementation.

![UML Class Diagram](OOPMyDate.png)

## Instance Variables

The `MyDate` class contains the following private instance variables:

- **year** (int): Between 1 and 9999.
- **month** (int): Between 1 (January) and 12 (December).
- **day** (int): Between 1 and 28, 29, 30, or 31 depending on the month and whether it's a leap year for February.

## Static Variables

The class also contains the following public static final variables:

- **MONTHS** (`String[]`): Array of month names.
- **DAYS** (`String[]`): Array of day names.
- **DAY_IN_MONTHS** (`int[]`): Array of the number of days in each month.

These static variables are initialized as shown and are used in the methods.

## Static Methods

The `MyDate` class includes the following public static methods:

### 1. `isLeapYear(int year)`
Returns `true` if the given year is a leap year. A year is a leap year if:
- It is divisible by 4 but not by 100, or
- It is divisible by 400.

### 2. `isValidDate(int year, int month, int day)`
Returns `true` if the given year, month, and day constitute a valid date. The month should be between 1 (Jan) and 12 (Dec), and the day should be valid for that month and year.

### 3. `getDayOfWeek(int year, int month, int day)`
Returns the day of the week as an integer:
- 0 for Sunday,
- 1 for Monday,
- ..., 
- 6 for Saturday.

## Constructor

The `MyDate` class has one constructor which takes 3 parameters: `year`, `month`, and `day`. It invokes the `setDate()` method to initialize the instance variables.

## Public Methods

The following public methods are defined in the `MyDate` class:

### 1. `setDate(int year, int month, int day)`
Invokes (calls) the static method `isValidDate()` to verify that the provided year, month, and day form a valid date.
- **Note**: If the date is invalid, it `raise ValueError("Invalid year, month, or day!")`.

### 2. `setYear(int year)`
Verifies that the given year is between 1 and 9999.

- **Note**: `raise ValueError("Invalid year!")` if the year is out of range.

### 3. `setMonth(int month)`
Verifies that the given month is between 1 and 12.
- **Note**: `raise ValueError("Invalid month!")`  if the month is out of range.

### 4. `setDay(int day)`
Verifies that the given day is between 1 and the maximum days in that month, considering leap years for February.
- **Note**: `raise ValueError("Invalid day!")`  if the day is invalid for the given month.

### 5. `getYear()`, `getMonth()`, `getDay()`
Returns the value of the year, month, and day, respectively.

### 6. `toString()`
Returns a string representation of the date in the format `"xxxday d mmm yyyy"`. For example: `"Tuesday 14 Feb 2012"`.

### 7. `nextDay()`
Updates the instance to the next day and returns the instance. For example:
- The next day after `31 Dec 2000` would be `1 Jan 2001`.

### 8. `nextMonth()`
Updates the instance to the next month and returns the instance. For example:
- The next month after `31 Oct 2012` would be `30 Nov 2012`.

### 9. `nextYear()`
Updates the instance to the next year and returns the instance. For example:
- The next year after `29 Feb 2012` would be `28 Feb 2013`.
- **Note**: `raise ValueError("Year out of range!")` if the year exceeds 9999.

### 10. `previousDay()`, `previousMonth()`, `previousYear()`
Similar to `nextDay()`, `nextMonth()`, and `nextYear()`, these methods update the instance to the previous day, month, or year, respectively.

---

## Additional Notes

- The class should properly handle leap years, months with different numbers of days, and the transition between years, months, and days.
- Make sure to handle exceptions and validations according to the Note requirements.


## Instructions

1. **Create/Modify `homework.py`:**


2. **Running the Script Normally:**
   - To run the script normally, open your terminal and navigate to the directory containing `homework.py`.
   - Execute the script using Python:
     ```sh
     python homework.py
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


This output indicates that both test cases have passed successfully. 
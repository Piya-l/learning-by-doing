# MyDate Class Assignment

The `MyDate` class models a date instance and includes methods for validating and manipulating dates. Below are the detailed requirements for the class.

> **Important Constraint**: You are **not allowed** to use any built-in Date/Time libraries (like `datetime`, `calendar`, etc.) for any part of this implementation. All logic must be calculated manually using the rules defined below.

![UML Class Diagram](OOPMyDate.png)

## 1. Calendar Standards & Constraints

To ensure all implementations behave identically, you must adhere to these specific rules:

* **Calendar System**: Use the **Gregorian Calendar** rules.
* **Valid Year Range**: Years must be between **1582** and **9999** (inclusive).
    * *Note*: 1582 is the year the Gregorian calendar was widely adopted.
* **Day of Week Reference**: To calculate the day of the week, you must use **Thursday, January 1st, 1970** as your reference point (epoch).
    * Calculations for dates before and after this reference point must derive the day of the week by counting the total days difference.

## 2. Instance Variables

The `MyDate` class must contain the following **private** instance variables:

-   `year` (int): Valid range [1582, 9999].
-   `month` (int): Valid range [1, 12].
-   `day` (int): Valid range [1, n], where n is the number of days in that specific month/year.

## 3. Static Variables

Initialize the following **public static final** variables exactly as shown:

-   `MONTHS`: `["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]`
-   `DAYS`: `["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]`
-   `DAYS_IN_MONTHS`: `[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`
    * *Implementation Note*: You must strictly use `DAYS_IN_MONTHS` for standard lookups. For Leap Years, you must manually override the days in February to 29.

## 4. Static Methods

### `isLeapYear(int year)`
Returns `true` if the year is a leap year; otherwise `false`.
* **Algorithm**: A year is a leap year if:
    1.  It is divisible by 4, AND
    2.  It is NOT divisible by 100, UNLESS
    3.  It is divisible by 400.

### `isValidDate(int year, int month, int day)`
Returns `true` only if:
* `year` is between 1582 and 9999.
* `month` is between 1 and 12.
* `day` is between 1 and the last valid day of that specific month (accounting for leap years).

### `getDayOfWeek(int year, int month, int day)`
Returns an integer representing the day of the week (0=Sunday, 1=Monday, ..., 6=Saturday).
* **Required Algorithm**:
    1.  Calculate the total number of days elapsed between the input date and the reference date (**Thursday, Jan 1, 1970**).
    2.  Adjust the reference day index (Thursday = 4) by the modulo of the total days.
    3.  Ensure the result handles negative differences (dates before 1970) correctly to return a positive index 0-6.

## 5. Constructor

### `MyDate(int year, int month, int day)`
* Calls the `setDate(year, month, day)` method.

## 6. Public Methods

### `setDate(int year, int month, int day)`
* Calls `isValidDate`.
* If valid, sets the instance variables.
* If invalid, `raise ValueError("Invalid year, month, or day!")`.

### `setYear(int year)`
* Validates range [1582, 9999].
* If invalid, `raise ValueError("Invalid year!")`.

### `setMonth(int month)`
* Validates range [1, 12].
* If invalid, `raise ValueError("Invalid month!")`.

### `setDay(int day)`
* Validates range [1, last day of current month].
* If invalid, `raise ValueError("Invalid day!")`.

### Getters
* `getYear()`, `getMonth()`, `getDay()`: Return the respective instance variables.

### `toString()`
* Returns a string formatted exactly as: `"Monday 1 Jan 2000"`.
* Format: `"[DayName] [day] [MonthName] [year]"`

---

### 7. Manipulation Methods (Logic Requirements)

These methods update the current instance (`self`) and return it. You must implement the specific **"Rollover"** and **"Clamping"** logic described below to handle invalid intermediate states.

### `nextDay()`
* **Logic**: Increment `day` by 1.
* **Rollover**:
    * If `day` > days in current month, reset `day` to 1 and increment `month`.
    * If `month` > 12, reset `month` to 1 and increment `year`.
* **Validation**: Check year bounds. If year > 9999, `raise ValueError("Year out of range!")`.

### `nextMonth()`
* **Logic**: Increment `month` by 1.
* **Rollover**: If `month` > 12, reset `month` to 1 and increment `year`.
* **Clamping (Skip Invalid)**: If the current `day` exceeds the number of days in the *new* month, clamp `day` to the last valid day of that new month.
    * *Case*: `31 Jan` -> `nextMonth()` -> `28 Feb` (or 29 Feb).
    * *Case*: `31 Mar` -> `nextMonth()` -> `30 Apr`.
* **Validation**: Check year bounds.

### `nextYear()`
* **Logic**: Increment `year` by 1.
* **Clamping (Skip Invalid)**: If current date is `29 Feb` and new year is not a leap year, clamp `day` to `28`.
* **Validation**: If year > 9999, `raise ValueError("Year out of range!")`.

### `previousDay()`
* **Logic**: Decrement `day` by 1.
* **Rollover**:
    * If `day` becomes 0, decrement `month`. Set `day` to the maximum days of that *new* month.
    * If `month` becomes 0, set `month` to 12 and decrement `year`.
* **Validation**: If year < 1582, `raise ValueError("Year out of range!")`.

### `previousMonth()`
* **Logic**: Decrement `month` by 1.
* **Rollover**: If `month` becomes 0, set `month` to 12 and decrement `year`.
* **Clamping (Skip Invalid)**: If current `day` > days in new month, clamp `day` to the max days of the new month.
    * *Case*: `31 Mar` -> `previousMonth()` -> `28 Feb`.
* **Validation**: Check year bounds.

### `previousYear()`
* **Logic**: Decrement `year` by 1.
* **Clamping (Skip Invalid)**: If date is `29 Feb` and previous year is not a leap year, clamp `day` to `28`.
* **Validation**: If year < 1582, `raise ValueError("Year out of range!")`.

---

## Instructions

1.  **Create `homework.py`**: Implement the class following the logic above strictly.
2.  **Test Execution**:
    To verify your strict adherence to the logic, run the test script:
    ```sh
    python chk_testcases.py
    ```
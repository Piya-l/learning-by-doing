import unittest
import io
import sys
import runpy
import os

def run_homework_with_input(input_str):
    """
    Run student's main.py with given input string.
    Handles both:
      - main.py defines main()
      - main.py runs code at top-level
    Returns captured stdout as string.
    """
    # Backup originals
    old_stdout = sys.stdout
    old_stdin = sys.stdin

    # Redirect stdin and stdout BEFORE import
    sys.stdout = io.StringIO()
    sys.stdin = io.StringIO(input_str)

    try:
        # Remove previous main module if exists
        if 'main' in sys.modules:
            del sys.modules['main']

        # Execute the student's main.py file directly to avoid name collisions.
        # This runs top-level code. Capture output produced during that execution.
        main_path = os.path.join(os.path.dirname(__file__), 'main.py')
        module_globals = runpy.run_path(main_path, run_name='main')
        output_after_import = sys.stdout.getvalue()

        # If executing the module produced no output, it's likely the student's
        # file defined `main()` but didn't call it (guarded with __name__).
        # In that case, call `main()` once. If the module already ran and
        # produced output (e.g. called `main()` unguarded), don't call again.
        if output_after_import.strip() == '':
            main_func = module_globals.get('main', None)
            if callable(main_func):
                main_func()

        # Get output
        output = sys.stdout.getvalue().strip()
    finally:
        # Restore originals
        sys.stdout = old_stdout
        sys.stdin = old_stdin

    return output

class TestHomework(unittest.TestCase):
    def test_homework_output_case1(self):
        input_str = '\n' # Mock empty/newline input as used in original chk_homework.py
        expected_output = """CashRegister Total: $270.73 Discount: $0.00 Total after discount: $270.73
CashRegister Total: $299.43 Discount: $59.89 Total after discount: $239.54
CashRegister Total: $197.63 Discount: $10.00 Total after discount: $187.63
CashRegister Total: $245.56 Discount: $49.11 Total after discount: $196.45
CashRegister Total: $304.27 Discount: $5.00 Total after discount: $299.27

...DONE TRANSACTION...

Summary Report
==================================================
Customer: John Doe
Level: Regular
Discount (%): 0
(SSWB002) Stainless Steel Water Bottle x 2 = 36.90
(YM005) Yoga Mat x 5 = 137.95
(FT009) Fitness Tracker x 1 = 59.99
(BS003) Bluetooth Speaker x 1 = 35.89
Total: 270.73
Discount: 0.00
==================================================
Customer: Any Name
Level: VIP
Discount (%): 20
(YM005) Yoga Mat x 2 = 55.18
(YM005) Yoga Mat x 5 = 137.95
(NCH008) Noise-Cancelling Headphones x 1 = 89.50
(ILB010) Insulated Lunch Bag x 1 = 16.80
Total: 299.43
Discount: 59.89
==================================================
Customer: Alice Smith
Level: Silver
Discount ($): 10
(WE001) Wireless Earbuds x 2 = 99.98
(LDL007) LED Desk Lamp x 1 = 42.30
(SSWB002) Stainless Steel Water Bottle x 3 = 55.35
Total: 197.63
Discount: 10.00
==================================================
Customer: Emily Davis
Level: VIP
Discount (%): 20
(NCH008) Noise-Cancelling Headphones x 2 = 179.00
(YM005) Yoga Mat x 1 = 27.59
(SS004) Smartphone Stand x 3 = 38.97
Total: 245.56
Discount: 49.11
==================================================
Customer: Charlie Brown
Level: Student
Discount ($): 5
(YM005) Yoga Mat x 1 = 27.59
(NCH008) Noise-Cancelling Headphones x 1 = 89.50
(FT009) Fitness Tracker x 2 = 119.98
(ILB010) Insulated Lunch Bag x 4 = 67.20
Total: 304.27
Discount: 5.00
==================================================
Total Transaction: 5.00
Total Sales: 1317.62
Total Discount: 124.00
=================================================="""
        
        output = run_homework_with_input(input_str)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

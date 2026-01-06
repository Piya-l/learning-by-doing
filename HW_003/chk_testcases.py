import unittest
import sys
import io
import os
import runpy
import math

class TestCoordinate(unittest.TestCase):
    def setUp(self):
        # Check if coordinate.py exists
        if not os.path.exists('coordinate.py'):
            self.fail("coordinate.py not found. Please create it.")
        
        # dynamic import
        try:
            from coordinate import Coordinate
            self.Coordinate = Coordinate
        except ImportError:
            self.fail("Could not import Coordinate class from coordinate.py")
        except AttributeError:
             self.fail("Coordinate class not found in coordinate.py")

    def test_init(self):
        c = self.Coordinate(1, 2, 3, 4)
        self.assertEqual(c.x, 1)
        self.assertEqual(c.y, 2)
        self.assertEqual(c.z, 3)
        self.assertEqual(c.w, 4)

    def test_str(self):
        c = self.Coordinate(1, 2, 3, 4)
        self.assertEqual(str(c), "<Coordinate is 1, 2, 3, 4>")

    def test_add(self):
        c1 = self.Coordinate(1, 2, 3, 4)
        c2 = self.Coordinate(5, 6, 7, 8)
        c3 = c1 + c2
        self.assertEqual(str(c3), "<Coordinate is 6, 8, 10, 12>")
        # Ensure it returns a NEW Coordinate instance
        self.assertIsInstance(c3, self.Coordinate)
        self.assertIsNot(c3, c1)
        self.assertIsNot(c3, c2)

    def test_sub(self):
        c1 = self.Coordinate(2, 3, 4, 5)
        c2 = self.Coordinate(5, 7, 9, 11)
        distance = c1 - c2
        expected_dist = math.sqrt((2-5)**2 + (3-7)**2 + (4-9)**2 + (5-11)**2)
        self.assertIsInstance(distance, float)
        self.assertAlmostEqual(distance, expected_dist)

    def test_eq(self):
        c1 = self.Coordinate(1, 2, 3, 4)
        c2 = self.Coordinate(1, 2, 3, 4)
        c3 = self.Coordinate(5, 6, 7, 8)
        self.assertTrue(c1 == c2)
        self.assertFalse(c1 == c3)
        self.assertFalse(c1 == "Not a coordinate") # Test type check

    def test_type_checks(self):
        c1 = self.Coordinate(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            c1 + "Not a coordinate"
        with self.assertRaises(TypeError):
            c1 - "Not a coordinate"

class TestMain(unittest.TestCase):
    def test_main_output(self):
        if not os.path.exists('main.py'):
            self.fail("main.py not found. Please create it.")

        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
             # Execute main.py
             runpy.run_path('main.py', run_name='__main__')
        except Exception as e:
            self.fail(f"main.py crashed with error: {e}")
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        
        # Expected output based on the instructions
        expected_snippets = [
            "c1 = <Coordinate is 2, 3, 4, 5>",
            "c2 = <Coordinate is 5, 7, 9, 11>",
            "c3 = c1 + c2 = <Coordinate is 7, 10, 13, 16>",
            "distance = c1 - c2 =", # Partial match to allow for float variation
            "c1 == Coordinate(2, 3, 4, 5) is True",
            "c1 == c2 is False"
        ]
        
        for snippet in expected_snippets:
            self.assertIn(snippet, output, f"Output should contain: '{snippet}'")

if __name__ == '__main__':
    unittest.main()

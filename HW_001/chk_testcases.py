import unittest
import subprocess
import sys

PYTHON_EXEC = sys.executable


class TestMainPy(unittest.TestCase):

    def run_program(self, user_input):
        result = subprocess.run(
            [PYTHON_EXEC, "main.py"],
            input=user_input,
            text=True,
            capture_output=True
        )
        return result.stdout

    def test_case_apple(self):
        user_input = "Apple\n"
        expected_output = (
            "Hello, what is your name: "
            "My name is Apple.\n"
            "From now on, I will submit all the homework and ensure it is on time. \\\"@_@\"/\n"
        )

        self.assertEqual(self.run_program(user_input), expected_output)

    def test_case_mr_white(self):
        user_input = "Mr. White\n"
        expected_output = (
            "Hello, what is your name: "
            "My name is Mr. White.\n"
            "From now on, I will submit all the homework and ensure it is on time. \\\"@_@\"/\n"
        )

        self.assertEqual(self.run_program(user_input), expected_output)


if __name__ == "__main__":
    unittest.main()

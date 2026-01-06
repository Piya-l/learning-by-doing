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
    maxDiff = 5000

    def test_add_shape(self):
        input_str = '1\nt\n5.0\n10.0\n5\n'
        expected_output = """Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the shape type (t for Triangle/r for Rectangle): Enter the width of the shape: Enter the height of the shape: Shape added successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Exiting..."""
        output = run_homework_with_input(input_str)
        self.assertEqual(output, expected_output)

    def test_update_shape(self):
        input_str = '1\nt\n5.0\n10.0\n2\n0\nr\n7.0\n14.0\n5\n'
        expected_output = """Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the shape type (t for Triangle/r for Rectangle): Enter the width of the shape: Enter the height of the shape: Shape added successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the index of the shape to update: Enter the new shape type (t for Triangle/r for Rectangle): Enter the new width of the shape: Enter the new height of the shape: Shape updated successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Exiting..."""
        output = run_homework_with_input(input_str)
        self.assertEqual(output, expected_output)

    def test_delete_shape(self):
        input_str = '1\nt\n5.0\n10.0\n3\n0\n5\n'
        expected_output = """Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the shape type (t for Triangle/r for Rectangle): Enter the width of the shape: Enter the height of the shape: Shape added successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the index of the shape to delete: Shape deleted successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Exiting..."""
        output = run_homework_with_input(input_str)
        self.assertEqual(output, expected_output)

    def test_display_shapes(self):
        input_str = '1\nt\n5.0\n10.0\n4\n1\nr\n5.1\n10.1\n4\n5\n'
        expected_output = """Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the shape type (t for Triangle/r for Rectangle): Enter the width of the shape: Enter the height of the shape: Shape added successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Shape 0 --> Shape Type: Triangle Width: 5.0 Height: 10.0 Area: 25.0
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the shape type (t for Triangle/r for Rectangle): Enter the width of the shape: Enter the height of the shape: Shape added successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Shape 0 --> Shape Type: Triangle Width: 5.0 Height: 10.0 Area: 25.0
Shape 1 --> Shape Type: Rectangle Width: 5.1 Height: 10.1 Area: 51.5
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Exiting..."""
        output = run_homework_with_input(input_str)
        self.assertEqual(output, expected_output)

    def test_combine(self):
        input_str = '''1
t
10.5
5.12
1
r
7.8
9.5
1
r
9.5
7.8
4
2
1
t
2.2
3.13
4
5
'''.replace('+', '')
        expected_output = """Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the shape type (t for Triangle/r for Rectangle): Enter the width of the shape: Enter the height of the shape: Shape added successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the shape type (t for Triangle/r for Rectangle): Enter the width of the shape: Enter the height of the shape: Shape added successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the shape type (t for Triangle/r for Rectangle): Enter the width of the shape: Enter the height of the shape: Shape added successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Shape 0 --> Shape Type: Triangle Width: 10.5 Height: 5.1 Area: 26.9
Shape 1 --> Shape Type: Rectangle Width: 7.8 Height: 9.5 Area: 74.1
Shape 2 --> Shape Type: Rectangle Width: 9.5 Height: 7.8 Area: 74.1
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Enter the index of the shape to update: Enter the new shape type (t for Triangle/r for Rectangle): Enter the new width of the shape: Enter the new height of the shape: Shape updated successfully!
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Shape 0 --> Shape Type: Triangle Width: 10.5 Height: 5.1 Area: 26.9
Shape 1 --> Shape Type: Triangle Width: 2.2 Height: 3.1 Area: 3.4
Shape 2 --> Shape Type: Rectangle Width: 9.5 Height: 7.8 Area: 74.1
Menu
1. Add a shape
2. Update a shape
3. Delete a shape
4. Display all shapes
5. Exit
Enter your choice: Exiting..."""

        output = run_homework_with_input(input_str)
        self.assertEqual(output, expected_output)

    def test_shape_methods_exist(self):
        from shape import Shape
        self.assertTrue(hasattr(Shape, 'print_info'), "Shape class should have a method named 'print_info'")
        self.assertTrue(hasattr(Shape, 'set_property'), "Shape class should have a method named 'set_property'")

    def test_shape_attributes_exist(self):
        from shape import Shape
        shape = Shape('t', 5.0, 10.0)
        self.assertTrue(hasattr(shape, '_Shape__shape_type'), "Shape class should have an attribute named '__shape_type'")
        self.assertTrue(hasattr(shape, '_Shape__width'), "Shape class should have an attribute named '__width'")
        self.assertTrue(hasattr(shape, '_Shape__height'), "Shape class should have an attribute named '__height'")

    # Add other tests here following the same pattern

if __name__ == '__main__':
    unittest.main()

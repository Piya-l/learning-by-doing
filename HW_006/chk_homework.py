import unittest
import io
import sys
import importlib

def loadhowework():
    # Import the homework script
    if 'homework' in sys.modules:
        importlib.reload(sys.modules['homework'])
    else:
        import homework

class TestHomework(unittest.TestCase):
    def test_homework_output_case1(self):
            expected_output = """Name: Line1, Color: Blue, Unit: cm, Length: 5.00 cm, Start Point: (0, 0), End Point: (3, 4)
Name: Rectangle1, Color: Red, Unit: m, Area: 50.00 m², Width: 5.00 m, Height: 10.00 m
Name: Square1, Color: Green, Unit: m, Area: 16.00 m², Side: 4.00 m
Name: Cube1, Color: Yellow, Unit: cm, Volume: 27.00 cm³, Edge Length: 3.00 cm
Name: Sphere1, Color: Purple, Unit: m, Volume: 65.45 m³, Radius: 2.50 m
Displaying all shapes:
Name: Line1, Color: Blue, Unit: cm, Length: 5.00 cm, Start Point: (0, 0), End Point: (3, 4)
Name: Rectangle1, Color: Red, Unit: m, Area: 50.00 m², Width: 5.00 m, Height: 10.00 m
Name: Square1, Color: Green, Unit: m, Area: 16.00 m², Side: 4.00 m
Name: Cube1, Color: Yellow, Unit: cm, Volume: 27.00 cm³, Edge Length: 3.00 cm
Name: Sphere1, Color: Purple, Unit: m, Volume: 65.45 m³, Radius: 2.50 m"""
        
            # Redirect stdout
            captured_output = io.StringIO()
            sys.stdout = captured_output
            
            # Mock stdin
            sys.stdin = io.StringIO('\n')

            # Import the homework script
            loadhowework()
            
            # Reset redirect.
            sys.stdout = sys.__stdout__
            
            # Check the output
            self.assertEqual(captured_output.getvalue().strip(), expected_output)

    
    
if __name__ == '__main__':
    unittest.main()
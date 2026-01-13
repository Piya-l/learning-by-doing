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
            expected_output = """Tuesday 28 Feb 2012
Wednesday 29 Feb 2012
Thursday 01 Mar 2012
Sunday 01 Apr 2012
Monday 01 Apr 2013
Monday 02 Jan 2012
Sunday 01 Jan 2012
Saturday 31 Dec 2011
Wednesday 30 Nov 2011
Tuesday 30 Nov 2010
Monday 28 Feb 2011
Invalid year, month, or day!
Invalid year, month, or day!"""
        
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
from main import mainApp
import unittest
import mock
import sys
from io import StringIO
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

class TestFunctional(unittest.TestCase):
    def test_c_11(self):
        with mock.patch('builtins.input', side_effect=["1", "B R2 B D R F D' R L B U2 F2 R F' R'", "0"]):
            captured_output = StringIO()
            sys.stdout = captured_output

            mainApp.play()

            sys.stdout = sys.__stdout__

            printed_output = captured_output.getvalue().strip()

            self.assertIn("solution", printed_output)
    
    def test_c_12(self):
        with mock.patch('builtins.input', side_effect=["1", "F2 L' R U D2 L' U F2 U2 L B' R' L' B'", "0"]):
            with self.assertRaises(Exception):
                mainApp.play()
    
    def test_c_13(self):
        with mock.patch('builtins.input', side_effect=["1", "F B2 U R' L F L' EROARE F D2 F' D' L B' D2'", "0"]):
            with self.assertRaises(Exception):
                mainApp.play()

    def test_c_211(self):
        with mock.patch('builtins.input', side_effect=["2", "1000", "y", "0"]):
            captured_output = StringIO()
            sys.stdout = captured_output

            mainApp.play()

            sys.stdout = sys.__stdout__

            printed_output = captured_output.getvalue().strip()
            self.assertIn("scramble generated:", printed_output)
            self.assertIn("solution", printed_output)

    def test_c_221(self):
        with mock.patch('builtins.input', side_effect=["2", "1001", "y", "0"]):
            with self.assertRaises(Exception):
                mainApp.play()

    def test_c_212(self):
        with mock.patch('builtins.input', side_effect=["2", "1000", "n", "0"]):
            captured_output = StringIO()
            sys.stdout = captured_output

            mainApp.play()

            sys.stdout = sys.__stdout__

            printed_output = captured_output.getvalue().strip()
            self.assertIn("scramble generated:", printed_output)

    def test_c_222(self):
        with mock.patch('builtins.input', side_effect=["2", "1001", "n", "0"]):
            with self.assertRaises(Exception):
                mainApp.play()

    def test_c_3(self):
        with mock.patch('builtins.input', side_effect=["3"]):
            captured_output = StringIO()
            sys.stdout = captured_output

            mainApp.play()

            sys.stdout = sys.__stdout__

            printed_output = captured_output.getvalue().strip()
            self.assertEqual(len(printed_output), 0) #verificam ca nu se afiseaza nimic deci programul se incheie
            
class TestStructural(unittest.TestCase):
    def test_s_1(self): #same as functional c_11
        with mock.patch('builtins.input', side_effect=["1", "B R2 B D R F D' R L B U2 F2 R F' R'", "0"]):
            captured_output = StringIO()
            sys.stdout = captured_output

            mainApp.play()

            sys.stdout = sys.__stdout__

            printed_output = captured_output.getvalue().strip()

            self.assertIn("solution", printed_output)
    
    def test_s_2(self):
        with mock.patch('builtins.input', side_effect=["1", "B R2 B D R F D' R L B U2 F2 R F' A'", "0"]):
            with self.assertRaises(Exception):
                mainApp.play()
    
    def test_s_3(self):
        with mock.patch('builtins.input', side_effect=["1", "B R2", "0"]):
            with self.assertRaises(Exception):
                mainApp.play()
    
    def test_s_4(self):
        with mock.patch('builtins.input', side_effect=["3"]):
            captured_output = StringIO()
            sys.stdout = captured_output

            mainApp.play()

            sys.stdout = sys.__stdout__

            printed_output = captured_output.getvalue().strip()
            self.assertEqual(len(printed_output), 0)

    def test_s_5(self):
        with mock.patch('builtins.input', side_effect=["2", "5", "y", "0"]):
            captured_output = StringIO()
            sys.stdout = captured_output

            mainApp.play()

            sys.stdout = sys.__stdout__

            printed_output = captured_output.getvalue().strip()
            self.assertIn("scramble generated:", printed_output)
            self.assertIn("solution", printed_output)

    def test_s_6(self):
        with mock.patch('builtins.input', side_effect=["2", "1005", "y", "0"]):
            with self.assertRaises(Exception):
                mainApp.play()

    def test_s_7(self):
        with mock.patch('builtins.input', side_effect=["2", "1000", "n", "0"]):
            captured_output = StringIO()
            sys.stdout = captured_output

            mainApp.play()

            sys.stdout = sys.__stdout__

            printed_output = captured_output.getvalue().strip()
            self.assertIn("scramble generated:", printed_output)

    def test_s_8(self):
        with mock.patch('builtins.input', side_effect=["2", "-3", "n", "0"]):
            with self.assertRaises(Exception):
                mainApp.play()
    


    


if __name__ == '__main__':
    unittest.main()
    # testerFunctional = TestFunctional()
    # testerFunctional.test_c_11()
    #testerFunctional.c_12()

# def yes_or_no():
#     answer = input("Do you want to quit? > ")
#     answer2 = input ("Mamaliga sau malai?: ")
#     if answer2 == "malai":
#         return("Quitter!")
#     elif answer == "no":
#         return("Awesome!")
#     else:
#         return("BANG!")


# def test_quitting():
#     with mock.patch('builtins.input', side_effect=["yes", "malai"]):
#         assert yes_or_no() == "Quitter!"

#     # with mock.patch('builtins.input', return_value="no"):
#     #     assert yes_or_no() == "Awesome!"
    
# test_quitting()

# def my_function():
#     print("Hello, world!")

# class TestPrintFunction(unittest.TestCase):
#     def test_print_output(self):
#         # Redirect stdout to capture printed output
#         captured_output = StringIO()
#         sys.stdout = captured_output

#         # Call the function that prints
#         my_function()

#         # Reset redirect
#         sys.stdout = sys.__stdout__

#         # Get the printed output
#         printed_output = captured_output.getvalue().strip()

#         # Assert that the expected output was printed
#         self.assertEqual(printed_output, "Hello, world!")


    
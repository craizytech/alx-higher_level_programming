#!/usr/bin/python3
"""This is the test module for 6-max_integer_test.py"""


import unittest
max_integer = __import__('6-max_integer_test').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class contains the test methods for the max integer function"""

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_list_with_int(self):
        self.assertEqual(max_integer([1,2,4]), 4)
    
    def test_list_with_nonint(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'a'])
    def test_list_negative_int(self):
        self.assertEqual(max_integer([-1,-2,-5,-6]), -1)
        self.assertEqual(max_integer([-1,-2, 3, 4]), 4)
    
    def test_list_one(self):
        self.assertEqual(max_integer([1]), 1)

if __name__ == "__main__":
    unittest.main()
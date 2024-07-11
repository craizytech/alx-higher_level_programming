#!/usr/bin/python3
"""This is the test module for 6-max_integer_test.py"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class contains the test methods for the max integer function"""

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_list_with_int(self):
        self.assertEqual(max_integer([1,2,4]), 4)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([1,2,3,4,5]),5)
        self.assertEqual(max_integer([6,2,3,4,5]),6)
        self.assertEqual(max_integer([1,2,6,4,5]),6)
        self.assertEqual(max_integer([-2,-1,-3,-4,-5]), -1)
        self.assertEqual(max_integer([1,2,-3,4,5]),5)
        self.assertEqual(max_integer([1.1, 2.3, 4.5, 6, 7.5]), 7.5)
        self.assertEqual(max_integer([-4]), -4)
    
    def test_list_with_nonint(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'a'])

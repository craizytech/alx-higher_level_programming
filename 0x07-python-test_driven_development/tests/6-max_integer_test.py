"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_onlyint_list(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1,2,3,4,5]), 5)
        self.assertEqual(max_integer([6,2,3,4,5]), 6)
        self.assertEqual(max_integer([1,2,6,4,5]), 6)
        self.assertEqual(max_integer([-1,-2,-6,-4,-5]), -1)
        self.assertEqual(max_integer([1,2,-3,4,5]), 5)
        self.assertEqual(max_integer([1.1, 2.3, 4.5, 6, 7.5]), 7.5)
    
    def test_parameters(self):
        self.assertRaises(TypeError, max_integer, [1,2,3], [3, 4, 5])
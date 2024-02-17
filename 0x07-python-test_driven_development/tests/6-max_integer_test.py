"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_onlyint_list(self):
        self.assertEqual(max_integer([1,2,3,4,5]), 5)
    
    def test_list_mixed(self):
        self.assertRaises(TypeError, max_integer,['a', 1, 'b', 2, 'c'])
    
    def test_list_float(self):
        self.assertEqual(max_integer([1.1, 2.3, 4.5, 6, 7.5]), 7.5)
    
    def test_parameters(self):
        self.assertRaises(TypeError, max_integer, [1,2,3], [3, 4, 5])
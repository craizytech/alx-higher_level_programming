#!/usr/bin/python3
"""This is the test method for the base class"""
from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    """This class tests the Base class"""

    def setUp(self):
        """Runs before each method is run"""
        self.instance_one = Base()
        self.instance_two = Base()
        self.instance_three = Base()
        self.instance_four = Base(12)

    def tearDown(self):
        """Runs after each method is run"""
        del(self.instance_one)
        del(self.instance_two)
        del(self.instance_three)
        del(self.instance_four)

    def test_private_attributes(self):
        """This method checks the private attributes of the class"""
        with self.assertRaises(AttributeError):
            self.instance_one.__nb_objects

    def test_id(self):
        """This method tests the id attribute"""
        self.assertEqual(self.instance_one.id, 1)
        self.assertEqual(self.instance_two.id, 2)
        self.assertEqual(self.instance_three.id, 3)
        self.assertEqual(self.instance_four.id, 12)
        self.assertNotEqual(self.instance_one, self.instance_three)

if __name__ == '__main__':
    unittest.main()

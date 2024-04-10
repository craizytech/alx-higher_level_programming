#!/usr/bin/python3
"""This is the base test module."""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """This tests the Base Class."""
    
    def test_private_attribute(self):
        """This method tests the private attributes."""
        obj1 = Base()
        # check if private attributes cannot be accesed
        with self.assertRaises(AttributeError):
            obj1.__nb_objects

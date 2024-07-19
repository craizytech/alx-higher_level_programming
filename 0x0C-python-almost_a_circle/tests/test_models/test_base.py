#!/usr/bin/python3
"""This is the test method for the base class"""
from models.base import Base
import unittest

class TestBaseInstantiation(unittest.TestCase):
    """This class tests instantiation of the Base class"""

    def test_no_arg(self):
        """This method tests the base when no Id is passed"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_None_id(self):
        """This method tests the base when the Id passed is None"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """This method tests the base when an object is instantiated with id"""
        self.assertEqual(67, Base(67).id)

    def test_when_given_id(self):
        """This method tests when an base is instantiated with an id"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_private_attributes(self):
        """Tests to ensure private attributes remain private"""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_many_args(self):
        """This method tests when more than enough arguments are passed"""
        with self.assertRaises(TypeError):
            Base(1, 2)
    

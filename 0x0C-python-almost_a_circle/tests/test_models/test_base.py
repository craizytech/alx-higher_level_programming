#!/usr/bin/python3
"""This is the base test module."""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """This tests the Base Class."""

    def setUp(self):
        """sets up all the required items for objects to work."""
        self.obj1 = Base();
        self.obj2 = Base();
        self.obj3 = Base(12);
        self.list_1 = [{"name": "Eammon"}, {"country":"Kenya"}, {"age":21}]
    
    def test_private_attribute(self):
        """This method tests the private attributes."""
        # check if private attributes cannot be accesed
        with self.assertRaises(AttributeError):
            self.obj1.__nb_objects

    def test_object_id(self):
        """This method tests the objects Id"""
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 2)
        self.assertEqual(self.obj3.id, 12)
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_to_json_string_with_lists(self):
        """Tests to_json_string method with a non-empty list."""
        json_string = Base.to_json_string(self.list_1)
        self.assertIsInstance(json_string, str)
    
    def test_to_json_string_with_empty_lists(self):
        """Tests the to_json_string method with []"""
        json_string = Base.to_json_string([])
        self.assertIsInstance(json_string, str)

    def test_to_json_string_with_none(self):
        """Tests the to_json_string with none."""
        json_string = Base.to_json_string(None)
        self.assertIsInstance(json_string, str)

    def test_from_json_string_with_a_string(self):
        """Tests the from_json_string with a json string."""
        json_string = Base.to_json_string(self.list_1)
        list_result = Base.from_json_string(json_string)
        self.assertEqual(self.list_1, list_result)

if __name__ == '__main__':
    unittest.main()

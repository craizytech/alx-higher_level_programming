#!/usr/bin/python3
"""This module tests the rectangle class"""
from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    """This class tests the rectangle class"""

    def setUp(self):
        """Runs before each method is run"""
        self.instance_one = Rectangle(1, 2, 3, 1)
        self.instance_two = Rectangle(5, 6, 7, 2)
        self.instance_three = Rectangle(9, 1, 2, 3)
        self.instance_four = Rectangle(4, 5, 6, 7, 4)
    
    def tearDown(self):
        """This method runs after each method is run"""
        del(self.instance_one)
        del(self.instance_two)
        del(self.instance_three)
        del(self.instance_four)
    
    def test_private_attributes(self):
        """This method checks that the instance attributes are inaccesible"""
        with self.assertRaises(AttributeError):
            self.instance_one.__nb_objects
        
        with self.assertRaises(AttributeError):
            self.instance_one.__width
        
        with self.assertRaises(AttributeError):
            self.instance_one.__height
        
        with self.assertRaises(AttributeError):
            self.instance_one.__x
        
        with self.assertRaises(AttributeError):
            self.instance_one.__y 

    def test_setter_methods(self):
        """Tests the rectangle width setter method"""
        
        with self.assertRaises(TypeError):
            self.instance_one.width = "string"
        
        with self.assertRaises(TypeError):
            self.instance_one.height = "string"
        
        with self.assertRaises(TypeError):
            self.instance_one.x = "string"
        
        with self.assertRaises(TypeError):
            self.instance_one.y = "tring"
        
        with self.assertRaises(ValueError):
            self.instance_one.width = -1

    def test_area_method(self):
        """Tests the rectangle area method"""

        self.assertEqual(self.instance_one.area(), 2)
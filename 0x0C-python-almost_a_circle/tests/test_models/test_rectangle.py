#!/usr/bin/python3
"""This module tests the rectangle class"""
from models.rectangle import Rectangle
from models.base import Base
import unittest

class TestRectangleInstantiation(unittest.TestCase):
    """This class tests the rectangle class"""
    
    def test_rectangle_is_base(self):
        """method checks to ensure that the rectangle is a base instance"""
        self.assertIsInstance(Rectangle(1, 2), Base)
    
    def test_no_args(self):
        """This method tests the rectangle with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Tests the rectangle method with one arg"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_arg(self):
        """Tests the rectangle method with two args"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Tests the rectangle with three args"""
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(4, 5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Tests the rectangle with four args"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """Tests the rectangle with five args"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        self.assertEqual(5, r1.id)
        self.assertEqual(10, r2.id)

    def test_more_than_five_args(self):
        """This method tests the rectangle with more than five args"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
    
    def test_width_private(self):
        """This method tests to ensure width private attr remains private"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 2, 3, 4)
            r1.__width

    def test_height_private(self):
        """This method tests to ensure height private attr remains private"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 2, 3, 4)
            r1.__height

    def test_x_private(self):
        """This method tests to ensure width private attr remains private"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 2, 3, 4)
            r1.__x

    def test_y_private(self):
        """This method tests to ensure width private attr remains private"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 2, 3, 4)
            r1.__y
    
    def test_width_getter(self):
        """This method tests the width getter method"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(1, r1.width)

    def test_width_setter(self):
        """This method tests the width setter method"""
        r1 = Rectangle(1, 2, 3, 4)
        r1.width = 12
        self.assertEqual(12, r1.width)

    def test_height_getter(self):
        """This method tests the height getter method"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(2, r1.height)
    
    def test_height_setter(self):
        """This method tests the height setter method"""
        r1 = Rectangle(1, 2, 3, 4)
        r1.height = 13
        self.assertEqual(13, r1.height)

    def test_x_getter(self):
        """This method tests the x getter method"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(3, r1.x)

    def test_x_setter(self):
        """This method tests the y setter method"""
        r1 = Rectangle(1, 2, 3, 4)
        r1.x = 12
        self.assertEqual(12, r1.x)

    def test_y_getter(self):
        """This method tests the x getter method"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(4, r1.y)

    def test_y_setter(self):
        """This method tests the y setter method"""
        r1 = Rectangle(1, 2, 3, 4)
        r1.y = 13
        self.assertEqual(13, r1.y)
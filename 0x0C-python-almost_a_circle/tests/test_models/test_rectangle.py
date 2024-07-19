#!/usr/bin/python3
"""This module tests the rectangle class"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
import io
import sys

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


class TestRectangle_width_Attribute(unittest.TestCase):
    """Unittests for testing the initialization of the width attribute"""

    def test_None_width(self):
        """Tests when None value is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
    
    def test_str_width(self):
        """Tests when string is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 4)
    
    def test_float_width(self):
        """Tests when float type is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.4, 2)
    
    def test_complex_width(self):
        """Tests when complex is passed as the value for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(3), 4)
    
    def test_dict_width(self):
        """This when a dictionary is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"one": 1, "two": 2}, 4)
    
    def test_bool_width(self):
        """This tests when a boolean is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 3)
    
    def test_list_width(self):
        """This tests when a list is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([3, 4, 5, 6], 7)
    
    def test_set_width(self):
        """This tests when a set is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 4)
    
    def test_tuple_width(self):
        """This tests when a tuple is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((3,), 4)
    
    def test_frozenset_width(self):
        """This method tests when a frozenset is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1,2}), 3)
    
    def test_range_width(self):
        """This method tests when a range object is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(3), 4)
    
    def test_bytes_width(self):
        """This tests when a binary string is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 5)
    
    def test_bytearray_width(self):
        """This method tests for when a bytearray  is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'Python'), 5)
    
    def test_memoryview_width(self):
        """This method tests when a memoryview is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'Python'), 5)
    
    def test_inf_width(self):
        """This method tests when infinity is passed for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)            
    
    def test_nan_width(self):
        """tests when nan is passed for the value of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 3)
    
    def test_negative_x(self):
        """Tests when a negative number is passed for x"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-11, 2)

class TestRectangle_height_Attribute(unittest.TestCase):
    """Unittests for testing the initialization of the height attribute"""

    def test_None_height(self):
        """Tests when None value is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None, 2)
    
    def test_str_height(self):
        """Tests when string is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "string", 4)
    
    def test_float_height(self):
        """Tests when float type is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 2.4, 2)
    
    def test_complex_height(self):
        """Tests when complex is passed as the value for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(3), 4)
    
    def test_dict_height(self):
        """This when a dictionary is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"one": 1, "two": 2}, 4)
    
    def test_bool_height(self):
        """This tests when a boolean is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True, 3)
    
    def test_list_height(self):
        """This tests when a list is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [3, 4, 5, 6], 7)
    
    def test_set_height(self):
        """This tests when a set is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3}, 4)
    
    def test_tuple_height(self):
        """This tests when a tuple is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (3,), 4)
    
    def test_frozenset_height(self):
        """This method tests when a frozenset is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1,2}), 3)
    
    def test_range_height(self):
        """This method tests when a range object is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(3), 4)
    
    def test_bytes_height(self):
        """This tests when a binary string is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python', 5)
    
    def test_bytearray_height(self):
        """This method tests for when a bytearray  is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'Python'), 5)
    
    def test_memoryview_height(self):
        """This method tests when a memoryview is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'Python'), 5)
    
    def test_inf_height(self):
        """This method tests when infinity is passed for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'), 2)            
    
    def test_nan_height(self):
        """tests when nan is passed for the value of height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'), 3)
    
    def test_negative_height(self):
        """Tests when a negative number is passed for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -11, 2)

class TestRectangle_x_Attribute(unittest.TestCase):
    """Unittests for testing the initialization of the x attribute"""

    def test_None_x(self):
        """Tests when None value is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)
    
    def test_str_x(self):
        """Tests when string is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "string", 4)
    
    def test_float_x(self):
        """Tests when float type is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 2.4)
    
    def test_complex_x(self):
        """Tests when complex is passed as the value for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(3), 4)
    
    def test_dict_x(self):
        """This when a dictionary is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"one": 1, "two": 2}, 4)
    
    def test_bool_x(self):
        """This tests when a boolean is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 3)
    
    def test_list_x(self):
        """This tests when a list is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [3, 4, 5, 6], 7)
    
    def test_set_x(self):
        """This tests when a set is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 4)
    
    def test_tuple_x(self):
        """This tests when a tuple is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (3,), 4)
    
    def test_frozenset_x(self):
        """This method tests when a frozenset is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1,2}))
    
    def test_range_x(self):
        """This method tests when a range object is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(3))
    
    def test_bytes_x(self):
        """This tests when a binary string is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')
    
    def test_bytearray_x(self):
        """This method tests for when a bytearray  is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'Python'))
    
    def test_memoryview_x(self):
        """This method tests when a memoryview is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'Python'))
    
    def test_inf_x(self):
        """This method tests when infinity is passed for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)            
    
    def test_nan_x(self):
        """tests when nan is passed for the value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 3)
    
    def test_negative_x(self):
        """Tests when a negative number is passed for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -1, 0)

class TestRectangle_y_Attribute(unittest.TestCase):
    """Unittests for testing the initialization of the y attribute"""

    def test_None_y(self):
        """Tests when None value is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)
    
    def test_str_y(self):
        """Tests when string is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "string")
    
    def test_float_y(self):
        """Tests when float type is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 2.4)
    
    def test_complex_y(self):
        """Tests when complex is passed as the value for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(3))
    
    def test_dict_y(self):
        """This when a dictionary is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"one": 1, "two": 2})
    
    def test_bool_y(self):
        """This tests when a boolean is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, True)
    
    def test_list_y(self):
        """This tests when a list is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [3, 4, 5, 6])
    
    def test_set_y(self):
        """This tests when a set is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {1, 2, 3})
    
    def test_tuple_y(self):
        """This tests when a tuple is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, (3,))
    
    def test_frozenset_y(self):
        """This method tests when a frozenset is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1,2}))
    
    def test_range_y(self):
        """This method tests when a range object is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(3))
    
    def test_bytes_y(self):
        """This tests when a binary string is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')
    
    def test_bytearray_y(self):
        """This method tests for when a bytearray  is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'Python'))
    
    def test_memoryview_y(self):
        """This method tests when a memoryview is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'Python'))
    
    def test_inf_y(self):
        """This method tests when infinity is passed for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('inf'))            
    
    def test_nan_y(self):
        """tests when nan is passed for the value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('nan'))
    
    def test_negative_y(self):
        """Tests when a negative number is passed for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -1)

class TestRectangle_area_method(unittest.TestCase):
    """Unittest for the Rectangle area method"""

    def test_area_small(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)
    
    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())
    
    def test_area_changed_attributes(self):
        r = Rectangle(1, 2)
        r.width = 3
        r.height = 4
        self.assertEqual(12, r.area())
    
    def test_area_one_arg(self):
        r = Rectangle(1, 2)

        with self.assertRaises(TypeError):
            r.area(1)

class TestRectangle_stdout(unittest.TestCase):
    """Unittest for testing the __str__ and the display methods of the Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """
        Capture and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout
            method (str): The method to run on rect
        
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture

        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture
    
    # Test the __str__ method
    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())
    
    def test_method_width_height_x(self):
        """tests the print with width, height, x attributes"""
        r = Rectangle(1, 2, 3)
        correct = "[Rectangle] ({}) 3/0 - 1/2".format(r.id)
        self.assertEqual(correct, str(r))

    def test_method_width_height_x_y(self):
        """tests the print with width, height, x, y attributes"""
        r = Rectangle(1, 2, 3, 4)
        correct = "[Rectangle] ({}) 3/4 - 1/2".format(r.id)
        self.assertEqual(correct, str(r))
    
    def test_method_width_height_x_y_id(self):
        """tests the print with width, height, x, y attributes"""
        r = Rectangle(1, 2, 3, 4, 5)
        correct = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(correct, str(r))
    
    def test_str_method_changed_attributes(self):
        """Tests when the attributes have been changed after instantiation"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 6
        r.height = 7
        r.x = 8
        r.y = 9
        self.assertEqual("[Rectangle] (5) 8/9 - 6/7", str(r))
    
    #Test the display method
    def test_display_width_height(self):
        """tests the display method with width and height"""
        r = Rectangle(2, 3, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())
    
    def test_display_width_height_x(self):
        """Tests the display method with width, height, x"""
        r = Rectangle(2, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("  ##\n  ##\n  ##\n", capture.getvalue())
    
    def test_display_width_height_y(self):
        """Tests the display method with width, height, y"""
        r = Rectangle(2, 3, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("\n##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x_y(self):
        """Tests the display method with width, height, y"""
        r = Rectangle(2, 3, 1, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("\n ##\n ##\n ##\n", capture.getvalue())
    
    def test_display_one_arg(self):
        """Tests the display method with one arg"""
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.display(1)
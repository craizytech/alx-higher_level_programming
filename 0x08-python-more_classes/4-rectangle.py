#!/usr/bin/python3
"""This module contains the implementation of the rectangle class."""


class Rectangle:
    """This is the rectangle class."""

    def __init__(self, width=0, height=0):
        """This is the constructor method.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """This is a getter method to retrieve value of width.

        Returns (int): The width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """This is the setter method for the width.

        Args:
            width (int):The width of the rectangle
        """
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """This is the getter method to retrieve the width.

        Returns (int): The height of the rectange
        """
        return self.__height

    @height.setter
    def height(self, height):
        """This is the setter method for the rectangle height.

        Args:
            height (int): The height of the rectangle
        """
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """This is a public instance method.

        Returns (int): returns the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """This is a public instance method.

        Args:
            returns the perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of the object.

        Returns (str): a rectangle filled with #"""

        if self.__height == 0 or self.__width == 0:
            return ""
        return '\n'.join(['#' * self.__width for i in range(self.__height)])

    def __repr__(self):
        """Shows official Object representation.
        Returns (str): The official object representation"""
        return f'Rectangle({self.__width}, {self.__height})'

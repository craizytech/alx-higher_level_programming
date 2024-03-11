#!/usr/bin/python3
"""This module defines a rectangle."""


class Rectangle:
    """This class defines a rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is the width getter."""
        return self.__width

    @property
    def height(self):
        """This is the height getter method."""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method returns the area of a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """This method returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """This method prints an informal representation on the object."""
        if self.__width == 0 or self.__height == 0:
            return 0

        result = ""
        for row in range(self.__height):
            for num in range(self.__width):
                result += "#"
            result += '\n'
        return result

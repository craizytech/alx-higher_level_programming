#!/usr/bin/python3
"""THis module defines a rectangle in using classes"""


class Rectangle:
    """This is the rectangle class."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is the width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is the width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif not value >= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is the height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif not value >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method returns the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """This method returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """returns an informal rep of the rectangle using # character"""

        rectangle = []

        for i in range(self.__height):
            rectangle.append("#" * self.__width + "\n")

        return ''.join(rectangle).rstrip()

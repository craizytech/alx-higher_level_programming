#!/usr/bin/python3
"""This module defines a rectangle."""


class Rectangle:
    """This class defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            return ""

        rect = []
        for row in range(self.__height):
            [rect.append(str(self.print_symbol)) for n in range(self.__width)]
            if row != self.__height - 1:
                rect.append('\n')
        return "".join(rect)

    def __repr__(self):
        """This method returns a formal representation of the object"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """This method is called when an object of the class is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

#!/usr/bin/python3
"""This is the rectangle module."""
from . import base


class Rectangle(base.Base):
    """This is the rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the constructor class."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Width Decorators
    @property
    def width(self):
        """This is the getter method for the width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """This is the width setter method."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Height decorators
    @property
    def height(self):
        """This is the height getter method."""
        return self.__height

    @height.setter
    def height(self, value):
        """This is the height setter method."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # X value decorators
    @property
    def x(self):
        """This is the x getter method."""
        return self.__x

    @x.setter
    def x(self, value):
        """This is the x setter method."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Y value Decorators
    @property
    def y(self):
        """This is the y getter method."""
        return self.__y

    @y.setter
    def y(self, value):
        """This is the y setter method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method calculates the area of the Rectangle."""
        return self.__height * self.__width

    def display(self):
        """This is a method that prints a representation of the rectangle."""
        print('\n' * self.__y, end="")
        for row in range(self.__height):
            print(" " * self.__x, end="")
            for pos in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """This is method prints the object representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

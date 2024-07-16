#!/usr/bin/python3
"""This module defines a rectangle that inherits from the base class"""
from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the constuctor class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """this is the width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is the width setter method"""
        if not type(value) is int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """This is the height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is the height setter method"""
        if not type(value) is int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """This is the x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """This is the setter for the x attribute"""
        if not type(value) is int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """This is the y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """This is the y setter method"""
        if not type(value) is int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """This method  returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance to the stdout"""
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width + '\n', end="")

    def __str__(self):
        """This method returns an informal representation of the object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

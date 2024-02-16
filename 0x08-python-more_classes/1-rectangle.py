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
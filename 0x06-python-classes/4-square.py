#!/usr/bin/python3
"""This is a square class implementation."""


class Square:
    """class contains the attributes methods that can be applied to a class."""
    def __init__(self, size=0):
        """This is the constructor class for the class Square object."""
        self.size = size

    @property
    def size(self):
        """This is the size getter method."""
        return self.__size

    @size.setter
    def size(self, value):
        """This is the size setter method."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the current area of the square."""
        return self.__size ** 2

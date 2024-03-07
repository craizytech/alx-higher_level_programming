#!/usr/bin/python3
"""This module defines a Class Square."""


class Square:
    """This class is used to define the properties of a square."""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This method calculates the area of the square."""
        return size ** 2

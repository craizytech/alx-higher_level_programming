#!/usr/bin/python3
"""This module creates the square class"""


class Square:
    """This is the Square class."""

    def __init__(self, size=0):
        """This is the constructor method"""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This method returns the area of a square"""
        return self.__size * self.__size

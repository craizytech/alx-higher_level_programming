#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """This defines a python class."""
    def __init__(self, size=0):
        """The init method of the Square class.

        Args:
            size : defines the size of the square
        """
        try:
            size = size + 0
        except TypeError:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

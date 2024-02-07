#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """This defines a python class."""
    def __init__(self, size=0):
        """The init method of the Square class.

        Args:
            size : defines the size of the square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

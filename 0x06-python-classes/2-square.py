#!/usr/bin/python3
"""This is a square class implementation."""


class Square:
    """class contains the attributes methods that can be applied to a class."""
    def __init__(self, size=0):
        """This is the constructor class for the class Square object."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

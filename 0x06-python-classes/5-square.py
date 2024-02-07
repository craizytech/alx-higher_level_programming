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

    @property
    def size(self):
        """int: returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This method calculates and returns the area of the square.

        Returns:
            area: The return value. The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints to the stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

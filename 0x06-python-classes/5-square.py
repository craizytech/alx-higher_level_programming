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

    @property
    def size(self):
        """This is the getter method for size."""
        return self.__size

    @size.setter
    def size(self, size):
        """This is the setter method for the size."""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This method calculates the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """This method prints out the square with #."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

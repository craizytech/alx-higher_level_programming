#!/usr/bin/python3
"""This module creates the square class"""


class Square:
    """This is the Square class."""

    def __init__(self, size=0):
        """This is the constructor method"""
        self.__size = size

    @property
    def size(self):
        """This is the size attribute getter."""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This method returns the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """This method prints out the square to the stdout using # character"""
        for i in range(self.__size):
            print("#" * self.__size)

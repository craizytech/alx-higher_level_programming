#!/usr/bin/python3
"""This module creates the square class"""


class Square:
    """This is the Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """This is the constructor method"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This is a position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """This is the position setter."""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method returns the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """This method prints out the square to the stdout using # character"""
        if self.__size == 0:
            print()
            return

        print('\n' * self.__position[1], end='')

        for i in range(self.__size):
            print(' ' * self.__position[0] + "#" * self.__size)

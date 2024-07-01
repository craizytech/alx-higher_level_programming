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

    def __eq__(self, other):
        """This method checks if two squares are equal based on the area"""
        return (self.__size ** 2) == (other.size ** 2)

    def __ne__(self, other):
        """This method checks if 2 squares are not equal based on the area"""
        return (self.__size ** 2) != (other.size ** 2)

    def __gt__(self, other):
        """This method checks of the 2 squares which is the bigger one"""
        return (self.__size ** 2) > (other.size ** 2)

    def __ge__(self, other):
        """This method checks if the square\
                is greater than or equal of the other square"""
        return (self.__size ** 2) >= (other.size ** 2)

    def __lt__(self, other):
        """This method checks wether the current\
                square is less than the other one"""
        return (self.__size ** 2) < (other.size ** 2)

    def __le__(self, other):
        """This method checks wether a square\
                is less than or equal to the other"""
        return (self.__size ** 2) <= (other.size ** 2)

#!/usr/bin/python3
"""This is a square module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is the square class."""
    def __init__(self, size):
        """This is a constructor class."""
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """This method returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """This method returns a string rep of a Square."""
        return f"[Rectangle] {self.__size}/{self.__size}"

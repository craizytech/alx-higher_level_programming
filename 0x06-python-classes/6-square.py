#!/usr/bin/python3
"""This is a square class implementation."""


class Square:
    """class contains the attributes methods that can be applied to a class."""
    def __init__(self, size=0, position=(0,0)):
        """This is the constructor class for the class Square object."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This is the size getter method."""
        return self.__size

    @size.setter
    def size(self, value):
        """This is the size setter method."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        """This is the position getter method."""
        return self.__position
    @position.setter
    def position(self, value):
        """This is the position setter method."""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers.""")
        if not isinstance(value[0], int) and not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers.""")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers.""")
        self.__position = value

    def area(self):
        """This method returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

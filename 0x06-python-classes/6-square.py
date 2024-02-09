#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """This defines a python class."""
    def __init__(self, size=0, position=(0, 0)):
        """The init method of the Square class.

        Args:
            size (int): defines the size of the square
            position (int): defines the position 
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

        if len(position) == 2 and isinstance(position, tuple):
            e = TypeError("position must be a tuple of 2 positive integers")
            if isinstance(position[0], int) and isinstance(position[1], int):
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    raise TypeError(e)
            else:
                raise TypeError(e)
        else:
            raise TypeError(e)
    @property
    def position(self):
        """int: returns the position."""
        return self.__position

    @position.setter
    def position(self, position):
        e = TypeError("position must be a tuple of 2 positive integers")
        if len(position) == 2 and isinstance(position, tuple):
            if isinstance(position[0], int) and isinstance(position[1], int):
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    raise TypeError(e)
            else:
                raise TypeError(e)
        else:
            raise TypeError(e)

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
        """if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

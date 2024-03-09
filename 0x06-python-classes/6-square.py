#!/usr/bin/python3
"""This module defines a Class Square."""


class Square:
    """This class is used to define the properties of a square."""
    def __init__(self, size=0, position=(0,0)):
        """This is the initialization function for the Square."""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        if isinstance(position[0], int) and\
                isinstance(position[1], int):
            if position[0] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                raise TypeError("position must\
                        be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        """This is the postion getter and setter."""
        return self.__position

    @position.setter
    def position(self, pos=(0,0)):
        """This is a setter method for the postion private attribute."""
        if isinstance(pos[0], int) and\
                isinstance(pos[1], int):
                    if pos[0] >= 0 and pos[1] >= 0:
                        self.__position = pos
                    else:
                        raise TypeError("position must\
                                be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
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
            print("")
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

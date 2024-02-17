#!/usr/bin/python3
"""This module contains a function that prints a square"""


def print_square(size):
    """This method takes in a positive integer size
    Then prints the square representation using # char

    Args:
        size (int): positive integer"""

    if isinstance(size, int):
        if size >= 0:
            for i in range(size):
                for j in range(size):
                    print("#", end="")
                print()
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")

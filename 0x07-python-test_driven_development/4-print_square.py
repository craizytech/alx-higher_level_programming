#!/usr/bin/python3
"""This module prints a square."""


def print_square(size):
    """
    This function prints a square using the characters '#'

    Args:
        size (int): this is the size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

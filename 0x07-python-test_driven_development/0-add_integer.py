#!/usr/bin/python3
"""This module contains a function that performs a sum and returns a value."""


def add_integer(a, b=98):
    """This methods takes 2 args sums them up and returns the value.

    Args:
        a (int or float): first argument
        b (int or float): second argument(optional, default = 98)

    Returns:
        int or float: the sum of the two arguments
    """
    if type(a) in [int, float]:
        a = int(a)
        if type(b) in [int, float]:
            b = int(b)
            return a + b
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")

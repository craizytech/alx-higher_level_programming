#!/usr/bin/python3
"""This module defines a magic class."""
from math import pi


class MagicClass:
    """This class is magical."""

    def __init__(self, value=0):
        """This method initializes the class."""
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """This method returns the area of a circle."""
        return (self.__radius ** 2) * pi

    def circumfrence(self):
        """This method returns the circumfrence of the circle."""
        return 2 * pi * self.__radius

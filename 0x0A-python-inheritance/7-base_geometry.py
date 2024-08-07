#!/usr/bin/python3
"""This module defines the class BaseGeometry"""


class BaseGeometry:
    """This class defines the base geometry"""

    def area(self):
        """This method returns the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates value"""

        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

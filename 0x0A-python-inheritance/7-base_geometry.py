#!/usr/bin/python3
"""This module defines a class base Geometry."""


class BaseGeometry:
    """This class contains geometry implementations."""

    def area(self):
        """This method calculates the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates an integer

        Args:
            name (string): this is the name of the value
            value (int): this is the value of the integer

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

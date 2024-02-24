#!/usr/bin/python3
"""This module defines a class base Geometry."""


class BaseGeometry:
    """This class contains geometry implementations."""

    def area(self):
        """This method calculates the area."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """This method validates an integer"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

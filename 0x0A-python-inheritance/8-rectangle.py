#!/usr/bin/python3
"""Rectaangle module."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class."""
    def __init__(self, width, height):
        """This is a constructor method."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

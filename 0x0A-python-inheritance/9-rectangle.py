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

    def area(self):
        """This method calculates and returns the area of the rectangle."""
        return self.__height * self.__width

    def __str__(self):
        """method returns the informal string representation of the rect."""
        return f"[Rectangle] {self.__width}/{self.__height}"

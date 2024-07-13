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
        """This method returns the area of an instance"""
        return self.__width * self.__height

    def __str__(self):
        """Returns an informal representation of the object"""
        return f"[Rectangle] {self.__width}/{self.__height}"

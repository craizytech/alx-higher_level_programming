#!/usr/bin/python3
"""This is the Square module."""
from . import rectangle


class Square(rectangle.Rectangle):
    """This is the Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the costructor class."""
        super().__init__(size, size, x, y, id)

    # width getter
    @property
    def width(self):
        """This is the width getter method"""
        return self.size
    
    # width setter method
    def width(self, size):
        """This is the with setter method"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
    
    # height getter method
    def height(self):
        """This is the height getter method"""
        return self.size
    
    # height setter method
    def height(self, size):
        """This is the height setter method"""
        if type(size) is not int:
            raise TypeError("height must be an integer")
        if size <= 0:
            raise ValueError("height must be > 0")
        self.height = size

    def __str__(self):
        """This is method prints the object representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

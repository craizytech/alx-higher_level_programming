#!/usr/bin/python3
"""This is the Square module."""
from . import rectangle


class Square(rectangle.Rectangle):
    """This is the Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the costructor class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This is method prints the object representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

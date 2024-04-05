#!/usr/bin/python3
"""This is the Square module."""
from . import rectangle


class Square(rectangle.Rectangle):
    """This is the Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the costructor class."""
        super().__init__(size, size, x, y, id)

    # size getter
    @property
    def size(self):
        """This is the width getter method"""
        return self.width
    
    # width setter method
    @size.setter
    def size(self, value):
        """This is the with setter method"""
        # if type(value) is not int:
        #     raise TypeError("size must be an integer")
        # if value <= 0:
        #     raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """This is method prints the object representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """This method updates the Attributes of the rectangle class.

        Args:
            args (tuple) : this tuple contains variable number of arguments
            kwargs (dict): dict containing keyword arguments
        """
        if len(args) > 0:
            self.id = args[0] if len(args) > 0 else self.id
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[3] if len(args) > 3 else self.x
            self.y = args[4] if len(args) > 4 else self.y
        else:
            for k, v in kwargs.items():
                self.id = v if k == "id" else self.id
                self.size = v if k == "size" else self.size
                self.x = v if k == "x" else self.x
                self.y = v if k == "y" else self.y

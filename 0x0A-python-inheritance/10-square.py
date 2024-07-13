#!/usr/bin/python3
"""This module inherits from Rectangle to create a Square Class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a square which inherits from Rectangle."""

    def __init__(self, size):
        """This is the constructor class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

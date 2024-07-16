#!/usr/bin/python3
"""This module defines a rectangle that inherits from the base class"""
from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the constuctor class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

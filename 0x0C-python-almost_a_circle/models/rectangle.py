#!/usr/bin/python3
"""This module defines a rectangle that inherits from the base class"""
from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the constuctor class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """this is the width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is the width setter method"""
        self.__width = value

    @property
    def height(self):
        """This is the height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is the height setter method"""
        self.__height = value

    @property
    def x(self):
        """This is the x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """This is the setter for the x attribute"""
        self.__x = value

    @property
    def y(self):
        """This is the y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """This is the y setter method"""
        self.__y = value

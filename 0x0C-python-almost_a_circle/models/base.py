#!/usr/bin/python3
"""This is the Base module."""


class Base:
    """This is the Base class used to create the almost a circle."""

    __nb_objects = 0
    
    def __init__(self, id=None):
        """This is the constructor method."""
        if id is not None:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects

#!/usr/bin/python3
"""This module defines the base class"""


class Base:
    """This is the base class of all the other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

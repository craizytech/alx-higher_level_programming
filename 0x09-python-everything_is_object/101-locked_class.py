#!/usr/bin/python3
"""This module defines a locked class"""


class LockedClass:
    """This class prevents a user form dynamically creating new instance
    attributes.
    """

    __slots__ = ()

    def __init__(self, first_name):
        self.first_name = first_name

    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value

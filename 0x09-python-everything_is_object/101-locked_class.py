#!/usr/bin/python3
"""This module defines a locked class"""


class LockedClass:
    """This class prevents a user form dynamically creating new instance
    attributes.
    """

    __slots__ = ('first_name',)

    def __init__(self, first_name):
        self.first_name = first_name

#!/usr/bin/python3
"""This module returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """This method returns a list of available attributes of an object

    Args:
        obj (object): The object whose attributes we need to obtain

    Returns:
        list containing the attributes and methods of that object"""

    return dir(obj)

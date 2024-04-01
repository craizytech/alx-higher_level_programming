#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """This method returns a list of available attributes of an object

    Args:
        obj (object): The object whose attributes we need to obtain

    Returns:
        list containing the attributes and methods of that object"""

    return dir(obj)

#!/usr/bin/python3
"""This function returns all the attributes of an object"""


def lookup(obj):
    """
    This method returns all the attributes and methods of an object

    Args:
        obj (object): This is the object we want to lookup

    Return: list of the attributes and methods
    """
    return dir(obj)

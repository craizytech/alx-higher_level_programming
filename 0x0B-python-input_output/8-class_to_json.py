#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    Function that returns the dictionary representation of a simple d/s

    Args:
        obj: the simple class object

    Returns: the dictionary representation of an object in JSON
    """
    return obj.__dict__

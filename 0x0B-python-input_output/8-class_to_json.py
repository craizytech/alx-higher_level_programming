#!/usr/bin/python3
"""This module dives into class objects."""


def class_to_json(obj):
    """This method returns the dict description of a object.

    Args:
        obj (class object): The oject to be converted to json

    Returns:
        the dictionary representation of an object
    """
    return obj.__dict__

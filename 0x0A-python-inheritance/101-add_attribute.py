#!/usr/bin/python3
"""Adding an attribute to an object."""


def add_attribute(obj, name, value):
    """This method adds a new attribute to an object if it's possible."""
    if not hasattr(obj, name):
        raise TypeError("[TypeError] can't add new attribute")
    setattr(obj, name, value)

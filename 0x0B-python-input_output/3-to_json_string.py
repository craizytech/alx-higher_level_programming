#!/usr/bin/python3
"""This module is used for serialization."""
import json


def to_json_string(my_obj):
    """This method converts a python object to a json string representation.

    Args:
        my_obj (object): This is a python object
    Returns:
        a json string representation of the my_object file
    """
    return json.dumps(my_obj)

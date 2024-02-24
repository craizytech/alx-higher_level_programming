#!/usr/bin/python3
"""This module desirializes a json object to a python object."""


import json


def from_json_string(my_str):
    """function that returns a JSON representation of an object.

    Args:
        my_str (json object): the json representation of an object

    Returns:
        Python object
    """
    return json.loads(my_str)

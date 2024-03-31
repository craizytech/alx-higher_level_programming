#!/usr/bin/python3
"""This is used to convert a python object to json."""
import json


def from_json_string(my_str):
    """This method converts a json object to a python object.

    Args:
        my_str (json object): This is a json object string representation
    Returns:
        a python object
    """
    return json.loads(my_str)

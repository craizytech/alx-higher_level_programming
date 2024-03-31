#!/usr/bin/python3
"""This module creates a python object from a json file."""
import json


def load_from_json_file(filename):
    """This method loads a python object from a json file.

    Args:
        filename (str): the name of filename to read the object from
    """
    with open(filename, "r", encoding="utf-8") as f:
        my_object = json.load(f)
    return my_object

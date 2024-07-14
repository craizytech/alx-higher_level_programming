#!/usr/bin/python3
"""Create object from an object string"""
import json


def load_from_json_file(filename):
    """
    This function creates a python object from a JSON file

    Args:
        filename: the name of the json file containing the python object
    """
    with open(filename, "r", encoding="utf-8") as file:
        json_string = file.read()
    return json.loads(json_string)

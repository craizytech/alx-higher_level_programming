#!/usr/bin/python3
"""This module creates an Object from a JSON File"""


import json


def load_from_json_file(filename):
    """This method returns a python object from a file containing Json.

    args:
        filename (string): the name of the file to be read.

    Returns a python object
    """
    with open(filename, mode="r", encoding="utf-8") as json_file:
        return json.load(json_file)

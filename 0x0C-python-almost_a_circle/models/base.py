#!/usr/bin/python3
"""This is the Base module."""
import json


class Base:
    """This is the Base class used to create the almost a circle."""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor method."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """This method converts the object list_dictionaries to a json string

        Args:
            list_dictionaries (obj): list of dictionaries.
        Returns:
            Json rep of list_dictionaries or None if list_dictionaried is None
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

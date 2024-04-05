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

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method converts the object list_dictionaries to a json string

        Args:
            list_dictionaries (obj): list of dictionaries.
        Returns:
            Json rep of list_dictionaries or None if list_dictionaried is None
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method saves the json obj rep of list_objs to a file

        Args:
            list_objs (object): list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as jsonfile:
            if list_objs is None:
                dict_list = []
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
            json_string = Base.to_json_string(dict_list)
            jsonfile.write(json_string)

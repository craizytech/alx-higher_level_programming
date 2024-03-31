#!/usr/bin/python3
"""Student class Module."""


class Student:
    """This class defines a student."""
    def __init__(self, first_name, last_name, age):
        """This is the constructor method of this class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this method retrieves a dictionary rep of a student instance."""
        if isinstance(attrs, list):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """This method replaces all the attributes of tje Student instance.
        Args:
            json (dict): dictionary containing the attributes of the instance
        """
        for k,v in json.items():
            setattr(self, k, v)

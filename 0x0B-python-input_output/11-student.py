#!/usr/bin/python3
"""Student to JSON module"""


class Student:
    """This class defines a student object"""

    def __init__(self, first_name, last_name, age):
        """This is the constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This method retrives the dictionary representation of the student
        instance

        Returns: The dictionary representation of the student instance
        """
        if type(attrs) is list:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        this method replaces all the attributes of Student instance

        Args:
            json (dictionary): dictionary containing attributes to replace
        """
        for k, v in json.items():
            self.__dict__[k] = v

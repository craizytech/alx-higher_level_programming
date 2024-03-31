#!/usr/bin/python3
"""Student class Module."""


class Student:
    """This class defines a student."""
    def __init__(self, first_name, last_name, age):
        """This is the constructor method of this class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this method retrieves a dictionary rep of a student instance."""
        return self.__dict__

#!/usr/bin/python3
"""This module defines a class that inherits from list class"""


class MyList(list):
    """This class is a subclass of List"""

    def __init__(self, my_list=None):
        """This is the constructor method for the class"""
        if my_list is None:
            my_list = []
        super().__init__(my_list)

    def print_sorted(self):
        """This method returns a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list

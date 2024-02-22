#!/usr/bin/python3
"""This module defines a class that inherits from list class"""


class MyList(list):
    """This class is a subclass of List"""

    def __init__(self, my_list=[]):
        """This is the constructor method for the class"""
        self.my_list = my_list

    def print_sorted(self):
        """This method returns a sorted list"""
        self.my_list = self.my_list.sort()
        print(self.my_list)
        return self.my_list

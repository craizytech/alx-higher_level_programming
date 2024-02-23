#!/usr/bin/python3
"""This module defines a class that inherits from list."""


class MyList(list):
    """This is a subclass of the list class."""

    def __init__(self, my_list=None):
        """The constructor method of this class."""
        if my_list is None:
            self.my_list = []
        else:
            self.my_list = my_list
        super().__init__(self.my_list)

    def print_sorted(self):
        """This method prints the list sorted."""
        sorted_list = sorted(self.my_list)
        print(sorted_list)
        return sorted_list

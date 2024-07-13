#!/usr/bin/python3
"""This module extends the list class"""


class MyList(list):
    """This class extends the list class"""
    def print_sorted(self):
        """"
        This method method prints the list in a sorted manner
        """
        print(sorted(self))

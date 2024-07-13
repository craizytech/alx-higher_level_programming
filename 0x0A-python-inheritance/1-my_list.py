#!/usr/bin/python3
"""This module extends the list class"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))

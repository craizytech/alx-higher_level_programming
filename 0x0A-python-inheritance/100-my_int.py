#!/usr/bin/python3
"""This module creates a class that inherits from int"""


class MyInt(int):
    """This class inherits from int and alters the magic methods"""

    def __eq__(self, other):
        """This magic method inverts the eq behaviour"""
        return super().__ne__(other)

    def __ne__(self, other):
        """This magic method inverts the ne behaviour"""
        return super().__eq__(other)

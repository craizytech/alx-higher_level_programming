#!/usr/bin/python3
"""The MyInt module."""


class MyInt(int):
    """MyInt that inherits from the int class."""
    def __eq__(self, other):
        """This is the magic method for the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """This is the magic method not equal to."""
        return super().__eq__(other)

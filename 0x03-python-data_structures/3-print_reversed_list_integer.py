#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    for x in my_list[::-1]:
        print("{:d}".format(x))
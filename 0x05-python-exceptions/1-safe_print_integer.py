#!/usr/bin/python3

def safe_print_integer(value):
    """This function prints an int .format."""
    try:
        print("{:d}".format(value))
        return True
    except:
        return False

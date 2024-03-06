#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """This function prints an integer."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception:", e, file=sys.stderr)
        return False

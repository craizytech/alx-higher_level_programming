#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer."""
    try:
        new_value = value / 0
    except ZeroDivisionError:
        if value != int(value):
            return False
        print("{:d}".format(value))
        return True
    except TypeError:
        return False

#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer."""
    try:
        new_value = value / 0
    except ZeroDivisionError:
        print("{:d}".format(value))
        return True
    except:
        return False

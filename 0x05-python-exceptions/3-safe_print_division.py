#!/usr/bin/python3
def safe_print_division(a, b):
    """Function that divides 2 integers and prints the result."""
    res = None
    try:
        res =  a / b
        return res
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(res))

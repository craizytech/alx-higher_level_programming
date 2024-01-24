#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Function that prints first x integer elements in a list."""
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            else:
                continue
        print()
    except IndexError:
        raise
    return count

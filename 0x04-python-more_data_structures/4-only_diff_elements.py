#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present only in one set."""
    diff = []
    for x in set_1:
        if x not in set_2:
            diff.append(x)
    for x in set_2:
        if x not in set_1:
            diff.append(x)
    return diff

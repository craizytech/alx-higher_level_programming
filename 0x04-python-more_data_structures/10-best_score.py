#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if a_dictionary is None or len(a_dictionary) == 0:
        return
    num = 0
    for i in a_dictionary:
        if a_dictionary[i] > num:
            key = i
            num = a_dictionary[i]
    return key

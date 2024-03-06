#!/usr/bin/python3

def best_score(a_dictionary):
    """This function returns a key with the biggest integer value."""
    max_value = float('-inf')
    max_key = None
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

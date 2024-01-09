#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character"""
    length = len(sentence)
    if length == 0:
        letter = None
    else:
        letter = sentence[0]
    return (length, letter)

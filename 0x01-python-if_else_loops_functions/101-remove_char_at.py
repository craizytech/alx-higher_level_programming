#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n > len(str) - 1:
        return str
    else:
        copy = ""
        for i in range(0, len(str)):
            if i != n:
                copy += str[i]
    return copy

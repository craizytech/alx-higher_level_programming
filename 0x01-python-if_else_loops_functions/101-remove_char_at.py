#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str) - 1:
        return str
    str_copy = []
    for char in str:
        if char == str[n]:
            continue
        str_copy.append(char)
    str_copy = "".join(str_copy)
    return str_copy

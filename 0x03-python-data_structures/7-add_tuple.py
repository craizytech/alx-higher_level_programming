#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 1 and len(tuple_b) > 1:
        sum = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif len(tuple_a) > 1 and len(tuple_b) == 1:
        sum = tuple_a[0] + tuple_b[0], tuple_a[1]
    elif len(tuple_a) == 1 and len(tuple_b) > 1:
        sum = tuple_a[0] + tuple_b[0], tuple_b[1]
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        sum = tuple_a[0], tuple_b[0]
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        sum = tuple_a[0], 0
    elif len(tuple_a) == 0 and len(tuple_b) == 1:
        sum = 0, tuple_b[0]
    elif len(tuple_a) == 0 and len(tuple_b) == 0:
        sum = 0, 0
    elif len(tuple_a) == 0:
        return tuple_b
    elif len(tuple_b) == 0:
        return tuple_a
    return sum

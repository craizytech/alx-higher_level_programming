#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight = 0
    div = 0
    for k, v in my_list:
        total_weight += (k * v)
        div += v
    return total_weight / div

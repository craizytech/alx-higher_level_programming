#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_list = sys.argv
    arg_count = len(sys.argv)
    sum = 0

    for i in range(1, arg_count):
        sum += int(arg_list[i])

    print(sum)

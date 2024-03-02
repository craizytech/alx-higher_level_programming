#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_list = sys.argv
    arg_count = len(sys.argv) - 1

    print(f"{arg_count} arguments:")
    for i in range(arg_count):
        print(f"{i}: {arg_list[i+1]}")

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_list = sys.argv
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("0 arguments.")
        exit(1)
    elif arg_count == 1:
        print("1 argument:")
        print(f"1: {arg_list[1]}")
        exit(1)

    print(f"{arg_count} arguments:")
    for i in range(1, arg_count+1):
        print(f"{i}: {arg_list[i]}")

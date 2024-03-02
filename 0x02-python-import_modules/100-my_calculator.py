#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_list = sys.argv
    arg_count = len(arg_list)

    print("Number of args:", arg_count)
    if arg_count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if arg_list[2] not in ['+', '-', '/', '*']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(arg_list[1])
    b = int(arg_list[3])

    if arg_list[2] == "+":
        print(f"{a} {arg_list[2]} {b} = {a + b}")
    elif arg_list[2] == "-":
        print(f"{a} {arg_list[2]} {b} = {a - b}")
    elif arg_list[2] == "*":
        print(f"{a} {arg_list[2]} {b} = {a * b}")
    elif arg_list[2] == "/":
        print(f"{a} {arg_list[2]} {b} = {a / b}")

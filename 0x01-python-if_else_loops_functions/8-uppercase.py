#!/usr/bin/python3
def uppercase(str):
    for c in str:
        num = ord(c)
        if 93 <= num <= 122:
            num -= 32
        print("{}".format(chr(num)), end="")
    print()

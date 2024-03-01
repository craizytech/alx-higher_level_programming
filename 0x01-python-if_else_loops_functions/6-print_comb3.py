#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            num = (i * 10) + j
            if num < 89:
                print("{:02d} ".format(num), end=",")
            else:
                print(" {:02d}".format(num))

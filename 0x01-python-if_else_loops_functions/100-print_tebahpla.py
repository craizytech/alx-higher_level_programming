#!/usr/bin/python3

flag = True
for i in range(122, 96 ,-1):
    if flag:
        flag = False
    else:
        flag = True
        i -= 32
    print("{}".format(chr(i)), end="")

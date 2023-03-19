#!/usr/bin/python3

for val in range(122, 96, -1):
    if val % 2 != 0:
        print("{}".format(chr(val - 32)), end='')
    else:
        print("{}".format(chr(val)), end='')

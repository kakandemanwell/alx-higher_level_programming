#!/usr/bin/python3


if __name__ == "__main__":
    """Prints the number of and the list of ts arguments"""
    import sys

    length = len(sys.argv)

    if length == 2:
        print("{} Argument".format(length - 1))
    else:
        print("{} Arguments".format(length - 1))

    for i in range(1, length):
        print("{}: {}".format(i, sys.argv[i]))

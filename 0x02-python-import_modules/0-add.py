#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the results of an addition"""

    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

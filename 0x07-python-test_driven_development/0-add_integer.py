#!/usr/bin/pyhton3

"""Defines an integer addition function"""


def add_integer(a, b=98):
    """Return the addition of a and b.
    all float arguments are casted to int
    return: ypeError upon failure. i.e not int or floats
    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

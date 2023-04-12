#!/usr/bin/python3

def safe_print_integer(value):
    """
    prints the integer value
    args: value(int): an integer to be printed
    return: True if value is integer,
           False if an error occurs
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

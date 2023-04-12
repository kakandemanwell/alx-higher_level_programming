#!/usr/bin/python3

def safe_print_integer_err(value):
    """safely prints the integer value and raises an exception if any!
    to the stdoutput"""
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr))
        return(None)

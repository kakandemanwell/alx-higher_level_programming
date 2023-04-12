#!/usr/bin/python3

def safe_print_division(a, b):
    """
    prints the division of two integers a, and b
    args:
    a(int), b(int): numerator and denominator integers respectively to divide
    return: the division result of a / b
    """
    try:
        division = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        division = None
    finally:
        print("Inside result: {:d}".format(division))

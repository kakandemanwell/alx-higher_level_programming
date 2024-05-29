#!/usr/bin/python3

if __name__ == "__main__":
    """
    imports all functions from the file calculator_1.py,
    and handles basic operations
    """
    from calculator_1 import add, sub, mul, div
    import sys
    argLength = len(sys.argv) - 1

    if argLength != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == '+':
        print("{:d} {} {:d} = {}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print("{:d} {} {:d} = {}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print("{:d} {} {:d} = {}".format(a, operator, b, mul(a, b)))
    else:
        print("{:d} {} {:d} = {}".format(a, operator, b, div(a, b)))

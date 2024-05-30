# !/usr/bin/python3
def safe_print_integer_err(value):
    """safely prints the integer value and raises an exception if any!
    to the stdoutput"""
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Extension: {}\n".format(e))
        return False
    else:
        return True

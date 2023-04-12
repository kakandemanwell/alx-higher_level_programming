#!/usr/bin/python3

def safe_function(fct, *args):
    """runs the function fct and prints an exception message
    to the stdoutput"""
    try:
        return(fct())
    except:
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr))
        return(None)

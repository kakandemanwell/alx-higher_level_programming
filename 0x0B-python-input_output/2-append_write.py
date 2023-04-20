#!/usr/bin/python3

"""Defines a function that apppends text to file"""


def append_write(filename="", text=""):
    """appends a text to a file, utf-8
    args:
        filename (str): name of file to write text to
        text (str): strings of text to append to file
    Return:
        Number of written characters
    """
    with open(filename, "a", encoding="utf-8") as f:
       return f.write(text)

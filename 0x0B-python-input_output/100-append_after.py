#!/usr/bin/python3

"""
defines a function that inserts text to
a file after a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a new_string in a file to replace a specific string
    args:
        filename (str): name of the file
        search_string (str): name of string to replace
        new_string (str): new string to append to file.
    """
    string = ""
    with open(filename) as f:
        for line in f:
            string += line
            if search_string in line:
                string += new_string
    with open(filename, 'w') as w:
        w.write(string)

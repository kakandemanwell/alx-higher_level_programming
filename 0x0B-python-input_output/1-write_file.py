#!/usr/bin/python3

"""Defines a function that appends text to an existing file."""


def write_file(filename="", text=""):
    """appends text to a read file using write
    Returns:
            Number of written characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

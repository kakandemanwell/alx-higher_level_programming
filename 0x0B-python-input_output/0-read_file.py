#!/usr/bin/python3

"""Defines a function that reads a file"""

def read_file(filename=""):
    """prints the contents of the read file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

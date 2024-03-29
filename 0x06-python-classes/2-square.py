#!/usr/bin/python3
"""defines a square class"""


class Square:
    """defines a square with a size dimension"""
    def __init__(self, size=0):
        """initializes a new square with size set to 0
        size: type(int)"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

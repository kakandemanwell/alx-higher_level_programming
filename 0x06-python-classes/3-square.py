#!/usr/bin/python3
"""defines a class square"""


class Square:
    """defines a square object with size set initially to 0"""
    def __init__(self, size=0):
        """initializes a square object with size set to 0
            size: type(int)"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            return (self.__size ** 2)

#!/usr/bin/python3
""" defines a class square"""


class square:
    """ defines a square of size size
    size: type(int)"""
    def __init__(self, size):
        """initializes a square object with size set to 0
        size: type(int)"""
        self.__size = size

    @property
    def size(self):
        """returns the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size to arg value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the class object"""
        return (self.__size ** 2)
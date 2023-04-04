#!/usr/bin/python3
""" defines a class square"""


class square:
    """ defines a square of size size
    size: type(int)"""
    def __init__(self, size):
        """initializes a square object with size set to 0"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError(" size must be > 0")
        self.__size = size

    @property
    def size(self):
        """returns the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size to arg value"""
        self.__size = value

    def area(self):
        return (self.__size ** 2)

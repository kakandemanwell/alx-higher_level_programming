#!/usr/bin/python3
""" defines a class square"""


class Square:
    """
    Initializes the Square with a sze.

    Parameters:
    size: (int): The size of the square. Default is 0.

    Raises:
    TypeError: if size is not an integer.
    ValueError: if size is less than 0.
    """
    def __init__(self, size):
        """
        Initializes the Square with a sze.

        Parameters:
        size: (int): The size of the square. Default is 0.

        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size to arg value"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the class object"""
        return self.__size ** 2

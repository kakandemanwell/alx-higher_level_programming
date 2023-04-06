#!/usr/bin/python3
"""defines a class Rectanlge"""


class Rectangle:
    """
    defines a Rectangle object with dimensions
    width: type(int) initialized at 0
    height: type(int) initialized at 0
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    """returns the value of the width parameter"""
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width to a value(int)"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """returns the value of the width parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height to a value(int)"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def __repr__():
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        rect = "Rectangle({}, {})".format(self.__width, self.__height)
        return rect

    def __del__(self):
        """returns a statement upon object deletion"""
        print("Bye rectangle...")

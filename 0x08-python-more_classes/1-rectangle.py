#!/usr/bin/python3
"""class definition of a recatngle"""


class Rectangle:
    """defines a rectangle with dimensions/parameters
    width and height as private instances
    """
    def __init__(self, width=0, height=0):
        """initialaizes a new tevtangle
        arguments;
        width -> int
        height -> int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """defines and sets the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """swts the wodth to a passed argument value(int)"""
        if not isintance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets the height to an initial value(0)"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height to a passed argument value
        value: int"""
        if isinstance(value, int):
            raise TypeError(" height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

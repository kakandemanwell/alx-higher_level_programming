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

    def area(self):
        """returns the area of the rectangle object"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter of the rectangle object"""
        if self.__height or self.__width is 0:
            return 0
        else:
            return (2(self.__height + self.__width))

    def __str__(self):
        """returns a visual representation of the rectangle
        using the character #"""
        if width == 0 or height == 0:
            print("")
        else:
            for height in range(self.__height):
                print('#'*self.__width)

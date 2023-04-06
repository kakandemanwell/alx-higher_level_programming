#!/usr/bin/python3
"""defines a class Rectanlge"""


class Rectangle:
    """
    defines a Rectangle object with dimensions
    width: type(int) initialized at 0
    height: type(int) initialized at 0
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        number_of_instances += 1

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
        """
        returns a visual representation of the
        rectangle using the character #
        """
        if width == 0 or height == 0:
            print("")
        else:
            for height in range(self.__height):
                print('#'*self.__width)

    def __repr__():
        """
        returns a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        rect = "Rectangle({}, {})".format(self.__width, self.__height)
        return rect

    def __del__(self):
        """deletes an object of the class"""
        print("Bye rectangle...")
        number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares and return the biggest of two rectangle
        objects depending on area.
        args:
            rect_1: type(Rectangle)
            rect_2: type(Rectangle)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_2.area() < rect_1.area():
            return rect_1
        else:
            return rect_2

    @staticmethod
    def square(cls, size=0):
        """returns a square of the rectangle object width==height==size"""
        return cls(size, size)

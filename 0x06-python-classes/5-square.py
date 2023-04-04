#!/usr/bin/python3
"""defines a class square"""


class square:
    """defines a square object with dimensions size"""
    def __init__(self, size=0):
        """initializes a class object with size set to 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be > 0")
        self.__size = size

    @property
    def size(self):
        """returns the size instance of the object"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size to value
        value: type(int)"""
        self.__size = value

    def area(self):
        """returns the area of the square object"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the figure of the object graphicaly using the character #"""
        if size == 0:
            print("")
        else:
            for height in range(self.__size):
                print('#'*self.__size)

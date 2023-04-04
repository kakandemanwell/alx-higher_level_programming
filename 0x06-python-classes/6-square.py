#!/usr/bin/python3
"""defines a class square"""


class square:
    """defines a square object with dimensions size"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes a class object with size set to 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be > 0")
        if not isinstance(position, tuple) and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """returns the size instance of the object"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size to value
        value: type(int)"""
        self.__size = value

    @property
    def position(self):
        """returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position to value
        vallue: type(tuple)"""
        self.__position = position

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

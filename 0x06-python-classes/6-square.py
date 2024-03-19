#!/usr/bin/python3
"""defines a class square"""


class Square:
    """A class to represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square with a size.

        Parameters:
        size (int): The size of the square. Default is 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        value (int): The size of the square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(tuple, value) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        prints the square with the character '#' in stdout.
        If size is equal to 0, prints an empty line.
        """
        if self.size == 0:
            print("")
        else:
            for h in range(self.__size):
                print(" " * self.__position, end="")
                print("#" * self.__size)

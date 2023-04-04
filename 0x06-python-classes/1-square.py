#!/usr/bin/python3

""" Defines a class Square! """


class Square:

    """ defines a square by;
        a private instance: size
        instantiation with size(no type/value verification) """

    def __init__(self, size):
        """ initializes the square class with a size parameter """

        self._size = size

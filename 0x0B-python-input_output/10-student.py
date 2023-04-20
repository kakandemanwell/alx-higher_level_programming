#!/usr/bin/python3

"""Defines a Student class"""


class Student:
    """Defines a student with a name and age"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation of a student"""
        if attrs is None:
            return self.__dict__
        else:
            namez = {}
            for attr, value in self.__dict__.items():
                if attr in attrs:
                    namez[attr] = value
        return namez

#!/usr/bin/python3

"""defines a class student"""


class Student:
    """defines a student with attributes
        firstname, last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """Initiates a 0student with a name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Return dictoinary representation of the class
        """
        return self.__dict__

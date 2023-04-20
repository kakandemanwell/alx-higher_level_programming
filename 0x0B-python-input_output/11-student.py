#!/usr/bin/python3

"""Defines a class Student"""


class Student:
    """creates an instance of student"""
    def __init__(self, first_name, last_name, age):
        """Initializes an instance of Student with
        args:
            fiest_name (str), last_name (str), age (int)
        """
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

    def reload_from_json(self, json):
        """Replaces all attributes of STudent with json contents
        args:
            json (dict): dictionary to replace the attributes
        """
        for k, v in json.items():
            setattr(self, k, v)

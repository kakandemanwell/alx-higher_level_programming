#!/usr/bin/python3

"""Defines a Json file deserialization function"""


import json


def load_from_json_file(filename):
    """
    creates a python object from a json file
    args:
        filename(str): file to serialize
    return:
        pyhton object.
    """
    with open(filename) as f:
        return json.load(f)

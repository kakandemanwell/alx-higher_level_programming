#!/usr/bin/python3

"""Defiines a class_to_json funtion"""


def class_to_json(obj):
    """returns the dictionary description of obj"""
    return obj.__dict__

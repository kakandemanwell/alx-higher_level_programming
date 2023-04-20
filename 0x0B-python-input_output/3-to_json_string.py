#!/usr/bin/python3

"""defines a function that serializes(string-to-json) a  python object to json"""

import json

def to_json_string(my_obj):
    """Return a changed python object my_obj to json"""
    return json.dumps(my_obj)

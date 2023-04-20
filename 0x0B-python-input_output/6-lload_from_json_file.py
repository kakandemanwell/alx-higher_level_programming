#!/usr/bin/python3

"""defines an object-creating function"""

import json

def load_from_json_file(filename):
    """creates an object(python) from a json file"""
    with open(filename) as f:
        return json.load(f)

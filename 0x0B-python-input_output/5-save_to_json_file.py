#!/usr/bin/python3
"""defines a save_to_json_file module"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using a JSON representation"""
    with open(filename, "w") as a_file:
        json.dump(my_obj, a_file)

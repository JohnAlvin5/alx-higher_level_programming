#!/usr/bin/python3
"""defines a from_json_string module"""

import json


def from_json_string(my_str):
    """returns an python data structure represented by a JSON string"""
    return (json.loads(my_str))

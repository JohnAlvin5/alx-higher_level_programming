#!/usr/bin/python3
"""defines a class student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a student instance
        (same as 8-class_to_json.py)
        """
        return (self.__dict__)

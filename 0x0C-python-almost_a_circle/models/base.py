#!/usr/bin/python3
"""defines a class base"""
import json


class Base:
    """defines a class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a
        file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as a_file:
            if list_objs is None:
                a_file.write("")
            else:
                list_dicts = [x.to_dictionary() for x in list_objs]
                a_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        new = cls(5, 5)
        new.update(**dictionary)
        return new

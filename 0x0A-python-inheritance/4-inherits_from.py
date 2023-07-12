#!/usr/bin/python3

"""defines a function"""


def inherits_from(obj, a_class):
    """returns true if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """
    return (issubclass(type(obj), a_class))

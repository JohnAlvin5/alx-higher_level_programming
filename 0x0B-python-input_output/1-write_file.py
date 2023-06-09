#!/usr/bin/python3
"""defines a write_file module"""


def write_file(filename="", text=""):
    """writes a string to a txt file (UTF8) and returns the number of
    characters written
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return (a_file.write(text))

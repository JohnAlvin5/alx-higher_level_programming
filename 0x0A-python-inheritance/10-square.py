#!/usr/bin/python3

"""Defines a class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class that inherits from Rectangle 9-rectangle.py"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

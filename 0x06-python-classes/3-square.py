#!/usr/bin/python3
"""defines a class square"""


class Square:
    """defines a class square."""
    def __init__(self, size):
        """Initialises a square.

        Args:
            size : size of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the current square."""
        return (self.__size * self.__size)

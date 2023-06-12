#!/usr/bin/python3
"""Defines a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initialise the Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of square"""
        return self.__size * self.__size

    def __str__(self):
        """Class string representation"""
        return "[{}] {}/{}".format(type(self).__name__, self.__size,
                                   self.__size)

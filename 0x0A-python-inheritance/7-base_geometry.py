#!/usr/bin/python3
"""Defines base class"""


class BaseGeometry():
    """Represents geometry base class"""

    def area(self):
        """Defines area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an integer greater than 0
        Args:
            name: integer name
            value: integer
        Raises:
            TypeError: if not an integer
            ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""Defines base class"""


class BaseGeometry():
    """Represents geometry base class"""

    def area(self):
        """Defines area method"""
        raise Exception("area() is not implemented")

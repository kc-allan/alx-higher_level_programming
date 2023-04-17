#!usr/bin/python3
"""Base Class"""


class Base:
    """Defines the base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        self.id = id
        Base.__nb_objects += 1

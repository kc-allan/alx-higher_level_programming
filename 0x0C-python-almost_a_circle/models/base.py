#!/usr/bin/python3
"""Def8nes a base class"""


class Base:
    """Represents Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes the class"""
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

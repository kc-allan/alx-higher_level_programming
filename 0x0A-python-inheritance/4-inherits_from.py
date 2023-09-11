#!/usr/bin/python3
"""Checks if obj inherits from a class"""


def inherits_from(obj, a_class):
    """Defines class checker"""

    if issubclass(obj, a_class) and type(obj) != a_class:
        return True
    return False

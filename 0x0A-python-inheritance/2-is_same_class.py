#!/usr/bin/python3
"""Checks if obj is of a class"""


def is_same_class(obj, a_class):
    """Defines class checker"""

    if type(obj) == a_class:
        return True
    return False

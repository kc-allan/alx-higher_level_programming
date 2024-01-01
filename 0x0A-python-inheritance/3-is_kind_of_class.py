#!/usr/bin/python3
"""Checks if obj is of a class oe inherits from a class"""


def is_kind_of_class(obj, a_class):
    """Defines class checker"""

    if isinstance(obj, a_class):
        return True
    return False

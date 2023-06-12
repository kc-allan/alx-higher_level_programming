#!/usr/bin/python3
"""Checks for class similarity"""


def is_same_class(obj, a_class):
    """Checks if class is the same
    Args:
        obj: object to be checked
        a_class: class comoared against
    """

    if type(obj) == a_class:
        return True
    return False

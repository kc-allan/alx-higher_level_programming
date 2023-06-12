#!/usr/bin/python3
"""Checks inheritance"""


def inherits_from(obj, a_class):
    """Checks inheritance
    Args:
        obj: object
        a_class: class
    Return: True/False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

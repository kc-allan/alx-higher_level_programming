#!/usr/bin/python3
"""Def8mes class kind checker"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class - checks if object is the same class kind
    a_class: class
    obj: object
    Returns: True/False
    """
    return isinstance(obj, a_class)

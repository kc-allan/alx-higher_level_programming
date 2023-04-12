#!/usr/bin/python3
"""K8nd of classes"""


def is_kind_of_class(obj, a_class):
    """checks if obj is of class or inherited from a_class"""
    if isinstance(obj, a_class):
        return True
    return False

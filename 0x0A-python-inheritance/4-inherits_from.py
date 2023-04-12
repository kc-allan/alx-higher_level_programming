#!/usr/bin/python3
"""Inherits from..."""


def inherits_from(obj, a_class):
    """Checks if obj inherits frim class"""
    if not type(obj) == a_class and isinstance(obj, a_class):
        return True
    return False

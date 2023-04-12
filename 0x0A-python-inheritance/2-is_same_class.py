#!/usr/bin/python3
"""Checks for class instances"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of class"""
    if type(obj) == a_class:
        return True
    return False

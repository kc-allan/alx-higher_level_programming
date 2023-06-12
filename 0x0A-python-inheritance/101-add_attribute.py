#!/usr/bin/python3
"""Attribute addition"""


def add_attribute(obj, name, value):
    """Adds new attribute"""

    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

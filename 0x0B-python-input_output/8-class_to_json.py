#!/usr/bin/python3
"""Class to Kson"""


def class_to_json(obj):
    """Returns dictionary representatiom"""
    return obj.__dict__

#!/usr/bin/python3
import json
"""Defines a string-to-JSON conversion function"""


def to_json_string(my_obj):
    """Return the JSON representation"""
    return json.dumps(my_obj)
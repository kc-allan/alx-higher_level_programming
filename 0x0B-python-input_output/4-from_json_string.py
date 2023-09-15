#!/usr/bin/python3
"""Converts JSON to object"""
import json


def from_json_string(my_str):
    """Returns object representation of a JSON string."""
    return json.loads(my_str)
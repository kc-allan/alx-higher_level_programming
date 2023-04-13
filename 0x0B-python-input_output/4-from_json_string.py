#!/usr/bin/python3
"""Json to text"""
import json


def from_json_string(my_str):
    """Converts json to plain text"""
    return json.loads(my_str)

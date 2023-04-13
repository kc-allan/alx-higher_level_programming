#!/usr/bin/python3
"""json to python"""
import json


def load_from_json_file(filename):
    """Json to python object"""
    with open(filename) as f:
        return json.load(f)

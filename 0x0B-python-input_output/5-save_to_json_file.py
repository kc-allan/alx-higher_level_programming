#!/usr/bin/python3
"""Saves json to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Save my_obj to filename"""
    with open(filename, "w") as f:
        json.dump(filename, f)

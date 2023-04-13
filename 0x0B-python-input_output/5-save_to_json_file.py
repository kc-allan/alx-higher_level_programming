#!/usr/bin/python3
"""Json to file"""
import json


def save_to_json_file(my_obj, filename):
    """Saves json object to file"""
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)

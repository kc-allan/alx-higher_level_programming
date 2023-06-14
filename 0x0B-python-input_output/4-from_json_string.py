#!/usr/bin/python3
"""Stting repredentation of a json obejct"""
import json


def from_json_string(my_str):
    """JSON to string"""
    return json.loads(my_str)

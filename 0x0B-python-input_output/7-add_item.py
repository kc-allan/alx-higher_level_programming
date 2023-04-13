#!/usr/bin/python3
"""Adds to a python list"""
import sys

if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        lst = load_from_json("add_item.json")
    except FileNotFoundError:
        lst = []
    lst.extend(sys.argv[1:])
    save_to_json(lst, "add_item.json")

#!/usr/bin/python3
"""Defines a file reading function"""


def read_file(filename=""):
    """Prints contents of a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
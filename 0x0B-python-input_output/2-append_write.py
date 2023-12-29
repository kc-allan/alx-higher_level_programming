#!/usr/bin/python3
"""Appends to a file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
#!/usr/bin/python3
"""Reads file"""


def read_file(filename=""):
    """Defines o9ening and reading a file"""

    with open(filename, "r", encoding="utf-8") as f:
        cont = f.read()
        print(cont)
    f.close()

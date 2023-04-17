#!/usr/bin/python3
"""Reads aa file"""


def read_file(filename="test.txt"):
    """Prints out file xontents"""
    filename = "test.txt"
    with open(filename, 'r') as f:
        for ch in filename:
            print(ch, end="")

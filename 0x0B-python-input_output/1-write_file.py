#!/usr/bin/python3
"""Edits a dilw"""


def write_file(filename="", text=""):
    """Inputs twxt into filename
    args:
        filename: file
        text: string to be written
    Return:
        no of qritten characters
    """
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)

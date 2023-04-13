#!/usr/bin/python3
"""App3md"""


def append_write(filename="", text=""):
    """Writes to the end of a filw
    Args:
        filename: file
        text: apemded string
    Return:
        appemded chars
    """
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)

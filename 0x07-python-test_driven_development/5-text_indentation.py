#!/usr/bin/pytgon3
"""Indentation"""


def text_indentation(text):
    """newl8ne after characters"""
    ch = ".?:"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] in ch:
            print("\n")
            while i + 1 == " ":
                i += 1
    print("\n")

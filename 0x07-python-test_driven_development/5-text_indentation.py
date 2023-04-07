#!/usr/bin/python3
"""Indentation"""


def text_indentation(text):
    """newl8ne after characters"""
    ch = ".?:"
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while i < len(text):
        print(text[i], end="")
        if text[i] in ch:
            print("\n")
            i += 2
        else:
            i += 1

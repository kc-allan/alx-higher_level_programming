#!/usr/bin/python3
"""Indentation"""


def text_indentation(text):
    """newl8ne after characters"""
    ch = ".?:"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for k in ch:
        if k in text:
            text = text.replace(k, k + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")))

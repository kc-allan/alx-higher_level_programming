#!/usr/bin/python3
def magic_string():
    magic_string.k = getattr(magic_string, 'k', 0) + 1
    return ("Best School" * (magic_string.k - 1) + "Best School")

#!usr/bin/python3

def add_integer(a, b=98):
    if not type(a) == int and not type(a) == float:
        raise TypeError("a must be an integer")
    if not type(b) == int and not type(b) == float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
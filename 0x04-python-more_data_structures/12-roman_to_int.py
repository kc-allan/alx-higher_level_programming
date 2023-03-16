#!/usr/bin/python3
from functools import reduce
def func(c1, c2):
    if c1 >= c2:
        return c1 + c2
    else:
        return c2 - c1
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == "":
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    numbers = []
    for i in roman_string:
        for k in romans:
            if i == k:
                numbers.append(romans[k])
                continue
    return reduce(func, numbers)

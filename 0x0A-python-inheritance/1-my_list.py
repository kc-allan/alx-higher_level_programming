#!/usr/bin/python3
"""Defines a class that inherits from lost"""


class MyList(list):
    """Represents class MyList"""

    def print_sorted(self):
        """Prints list elements in ascending order"""
        print(sorted(self))

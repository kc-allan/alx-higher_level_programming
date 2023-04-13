#!/usr/bin/python3
"""Inheritance frim lost"""


class MyList(list):
    """Defines list inheritance"""
    def print_sorted(self):
        return(sorted(self.copy()))

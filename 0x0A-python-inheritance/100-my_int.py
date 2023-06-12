#!/usr/bin/python3
"""Defines MyInt"""


class MyInt(int):
    """Represents MyInt"""

    def __eq__(self, other):
        """Overrides equal to"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overrides not ewual to"""
        return int(self) == int(other)

#!/usr/bin/python3

"""Define class Square with private attribute"""


class Square:
    """Square with private attribute siz"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

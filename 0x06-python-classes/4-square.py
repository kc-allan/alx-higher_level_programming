#!/usr/bin/python3

"""Define class Square with private attribute"""


class Square:
    """Square with private attribute siz"""
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
    def area(self):
        return self.__size * self.__size

#!/usr/bin/python3
"""Defines a rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle
       Attr:
            width: width of the rectangle.
            height: height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

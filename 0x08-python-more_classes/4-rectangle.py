#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Represents the rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize Rectangle


        args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Width getter/setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter/setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Parses string"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for k in range(self.__width):
                rect += "#"
            if i + 1 != self.__height:
                rect += "\n"
        return rect

    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect
        return rect

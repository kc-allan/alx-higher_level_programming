#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes rectangles"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter/setter"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter/setter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.width * 2

    def __str__(self):
        """Prints rectangle using #"""
        if self.__height == 0 or self.__width == 0:
            return ("")

        draw = []
        for i in range(self.__height):
            [draw.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                draw.append("\n")
        return ("".join(draw))

    def __repr__(self):
        """Return string representation of a Rectangle"""
        draw = "Rectangle(" + str(self.__width)
        draw += ", " + str(self.__height) + ")"
        return draw

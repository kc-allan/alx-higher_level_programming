#!/usr/bin/python3
"""Define a rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents the rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle
        args:
            width: width of the rectangle
            height: height of the rectangle
            x: x position
            y: y position
            id: id from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x setter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks for the larger rectangle
        Args:
            rect_1: first rectangle object
            rect_2: second rectangle object
        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectang    le")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        return rect_2

    def __str__(self):
        """Parses string"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = []
        for i in range(self.__height):
            for k in range(self.__width):
                rect.append(str(self.print_symbol))
            if i + 1 != self.__height:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """String representation"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Instance when Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

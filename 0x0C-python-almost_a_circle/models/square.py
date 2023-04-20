#!/usr/bin/python3
"""Defines a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square initialization"""
        super().__init(id, size, size, x, y)

    def __str__(self):
        return f"[Square] (self.id) self.x/self.y - self.height"
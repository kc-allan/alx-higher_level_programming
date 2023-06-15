#!/usr/bin/python3
"""Defines a  Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student.

        Args:
            first_name: First name
            last_nam: Surname
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representation of Student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

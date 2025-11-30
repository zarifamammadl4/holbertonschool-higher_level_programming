#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes in this list are included.
        """
        if isinstance(attrs, list) and all(
            isinstance(a, str) for a in attrs
        ):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

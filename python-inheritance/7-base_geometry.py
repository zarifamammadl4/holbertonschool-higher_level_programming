#!/usr/bin/python3
"""
Module that defines the BaseGeometry class with validation.
"""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
           raise TypeError(f"{name} must be an integer")
        if value <= 0:
           raise ValueError(f"{name} must be greater than 0")

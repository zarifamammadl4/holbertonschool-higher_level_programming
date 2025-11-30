#!/usr/bin/python3
"""
This module defines the BaseGeometry class with:
- an unimplemented area method
- an integer_validator method
"""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise an exception indicating the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is an integer greater than 0.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

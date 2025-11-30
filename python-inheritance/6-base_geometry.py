#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise an exception indicating the area method is not implemented."""
        raise Exception("area() is not implemented")

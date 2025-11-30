#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from BaseGeometry.
"""

BaseGeometry = __import__(7-base_geometry).BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the Rectangle with width and height.

        Both width and height must be positive integers validated
        by the integer_validator method.
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width  # Private attribute
        self.__height = height  # Private attribute

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

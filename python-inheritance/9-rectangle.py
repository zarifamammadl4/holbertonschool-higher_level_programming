#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle (must be > 0).
            height (int): The height of the rectangle (must be > 0).
        """
        self.integer_validator("width", width)   # Validate width
        self.__width = width                      # Private width attribute
        self.integer_validator("height", height) # Validate height
        self.__height = height                    # Private height attribute

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


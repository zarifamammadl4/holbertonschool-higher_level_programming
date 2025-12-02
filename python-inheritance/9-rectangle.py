#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the Square with size.

        The size is validated by integer_validator.
        """
        self.integer_validator("size", size)  # Validate size
        self.__size = size  # Private attribute
        super().__init__(size, size)  # Pass size as both width and height to the parent (Rectangle)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size  # or use self.__width * self.__height, inherited from Rectangle

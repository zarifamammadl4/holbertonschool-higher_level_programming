#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""

Rectangle = __import__(9-rectangle).Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the Square with size.

        The size is validated by integer_validator.
        """
        # Validate size
        self.integer_validator("size", size)
        # Private attribute
        self.__size = size
        # Pass size as both width and height to the parent (Rectangle)
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        # or use self.__width * self.__height, inherited from Rectangle
        return self.__size * self.__size

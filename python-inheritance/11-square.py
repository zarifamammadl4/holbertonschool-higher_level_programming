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
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # width and height are both size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

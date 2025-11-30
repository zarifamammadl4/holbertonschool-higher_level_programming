#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a specified class or an instance of a class that inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or an instance
    of a class that inherits from a_class, otherwise False.
    """
    return isinstance(obj, a_class)

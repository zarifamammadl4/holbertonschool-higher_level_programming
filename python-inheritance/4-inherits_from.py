#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class that inherits (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherits from
    a_class, but not if obj is exactly an instance of a_class.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)

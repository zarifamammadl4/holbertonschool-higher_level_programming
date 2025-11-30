#!/usr/bin/python3
"""
This module defines a function that returns a dictionary
description with simple data structure for JSON serialization
of an object.
"""


def class_to_json(obj):
    """
    Returns a dictionary containing all attributes of an object
    that are JSON-serializable (list, dict, str, int, bool).

    Args:
        obj: The object to be serialized.

    Returns:
        dict: Dictionary representation of obj's attributes.
    """
    return obj.__dict__.copy()

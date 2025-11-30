#!/usr/bin/python3
"""
This module defines a function that converts a Python object to a JSON string.
"""

def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return str(my_obj).replace("True", "true").replace("False", "false").replace("None", "null")

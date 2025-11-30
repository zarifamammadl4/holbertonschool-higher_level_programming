#!/usr/bin/python3
"""Function that converts a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string.

    Args:
        my_str (str): JSON string to convert.

    Returns:
        object: Resulting Python data structure.
    """
    return json.loads(my_str)

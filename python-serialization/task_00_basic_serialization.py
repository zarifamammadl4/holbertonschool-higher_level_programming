#!/usr/bin/env python3
"""Basic serialization and deserialization module"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the output JSON file
    """
    try:
        with open(filename, w, encoding=utf-8) as f:
            json.dump(data, f)
        return True
    except (TypeError, OSError) as e:
        print(f"Serialization failed: {e}")
        return False


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it to a Python dictionary.

    Args:
        filename (str): Name of the input JSON file

    Returns:
        dict: Python dictionary representing the JSON data
    """
    try:
        with open(filename, r, encoding=utf-8) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        print(f"Deserialization failed: {e}")
        return None

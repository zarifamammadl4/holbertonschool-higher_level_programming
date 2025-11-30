#!/usr/bin/python3
"""Basic serialization and deserialization module"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the file to save the JSON data
    """
    with open(filename, w, encoding=utf-8) as f:  # w is a string literal
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it to a Python dictionary.

    Args:
        filename (str): Name of the JSON file to read

    Returns:
        dict: Python dictionary representing the JSON data
    """
    with open(filename, r, encoding=utf-8) as f:
        return json.load(f)

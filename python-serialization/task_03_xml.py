#!/usr/bin/python3
"""Serializing and deserializing Python dictionaries to/from XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save to a file.

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The output XML filename
    """
    root = ET.Element("data")  # Root element

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML stores everything as text

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): The XML filename to read

    Returns:
        dict: The deserialized Python dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text  # All XML data is text

        return result
    except (ET.ParseError, FileNotFoundError):
        return {}

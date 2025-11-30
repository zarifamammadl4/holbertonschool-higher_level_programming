#!/usr/bin/python3
"""Pickle serialization and deserialization for a custom class"""

import pickle


class CustomObject:
    """Custom class with name, age, and is_student attributes"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle

        Args:
            filename (str): File to write the pickled object
        """
        try:
            with open(filename, wb) as f:  # wb must be a string
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject from a file using pickle

        Args:
            filename (str): File to read the pickled object

        Returns:
            CustomObject | None: Returns the object or None if error occurs
        """
        try:
            with open(filename, rb) as f:  # rb must be a string
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None

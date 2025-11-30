#!/usr/bin/python3
"""Serialization and deserialization using pickle"""

import pickle


class CustomObject:
    """Custom object with name, age, and is_student attributes"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes in the specified format"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the instance to a file using pickle

        Args:
            filename (str): Path of the file to save the serialized object
        Returns:
            None if an exception occurs, otherwise nothing
        """
        try:
            with open(filename, wb) as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError, IOError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file using pickle

        Args:
            filename (str): Path of the file to load the serialized object from
        Returns:
            An instance of CustomObject or None if an error occurs
        """
        try:
            with open(filename, rb) as f:
                obj = pickle.load(f)
            # Optional: ensure that the loaded object is an instance of CustomObject
            if isinstance(obj, cls):
                return obj
            return None
        except (FileNotFoundError, pickle.PickleError, IOError):
            return None

# task_01_pickle.py
import pickle
import os

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object’s attributes in the required format"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(fIs Student: {self.is_student})

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        If any error occurs, do not create the file.
        """
        try:
            with open(filename, wb) as f:
                pickle.dump(self, f)
        except Exception:
            # Fail silently as per instructions
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.
        If any error occurs (file missing or corrupted), return None
        """
        if not os.path.exists(filename):
            return None
        try:
            with open(filename, rb) as f:
                obj = pickle.load(f)
            # Ensure the object is actually a CustomObject instance
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None

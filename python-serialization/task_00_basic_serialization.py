# task_00_basic_serialization.py
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    
    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the file to save JSON data
    """
    if not isinstance(data, dict):
        raise ValueError("Provided data must be a dictionary.")
    
    try:
        with open(filename, w, encoding=utf-8) as f:  # Fixed: w and utf-8 as strings
            json.dump(data, f, indent=4)
    except TypeError as e:
        raise ValueError(f"Data contains non-serializable objects: {e}")
    except Exception as e:
        raise IOError(f"Error writing to file {filename}: {e}")

def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.
    
    Args:
        filename (str): Name of the JSON file to read from
        
    Returns:
        dict: Deserialized Python dictionary
    """
    try:
        with open(filename, r, encoding=utf-8) as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError(f"JSON content is not a dictionary: {data}")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} does not exist.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file {filename}: {e}")
    except Exception as e:
        raise IOError(f"Error reading from file {filename}: {e}")

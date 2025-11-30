# task_00_basic_serialization.py
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    
    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the file to save JSON data
    """
    try:
        with open(filename, w) as f:
            json.dump(data, f, indent=4)  # indent for readability
    except TypeError as e:
        raise ValueError(f"Data provided is not JSON serializable: {e}")
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
        with open(filename, r) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} does not exist.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file {filename}: {e}")
    except Exception as e:
        raise IOError(f"Error reading from file {filename}: {e}")

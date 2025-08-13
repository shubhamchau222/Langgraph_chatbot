import yaml
from pathlib import Path
import os
from types import SimpleNamespace


def read_yaml(filePath:str):
    """
    Loads a YAML configuration file and returns it as a dictionary.
    
    Args:
        file_path (str): Path to the YAML file.
    
    Returns:
        dict: Parsed YAML content.
    
    Raises:
        FileNotFoundError: If the file doesn't exist.
        yaml.YAMLError: If the YAML is invalid.
    """
    if not os.path.exists(filePath):
        raise FileNotFoundError(f"Config file not found: {filePath}")

    with open(filePath, mode="r") as file:
        try:
            data= yaml.safe_load(file)
            # return SimpleNamespace(data)
            return data
        except Exception as e:
            raise yaml.YAMLError(f"Error parsing YAML file {filePath}: {e}")


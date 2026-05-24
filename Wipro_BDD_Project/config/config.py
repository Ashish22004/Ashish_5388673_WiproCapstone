# Import yaml library to read .yaml files
import yaml

# Import os library to handle file paths
import os


# Class to handle loading configuration
class Config:

    # Static method - no need to create object to call this
    @staticmethod
    def load_config():

        # Build full path to qa.yaml file (same folder as this file)
        config_path = os.path.join(
            os.path.dirname(__file__), "qa.yaml"
        )

        # Open qa.yaml and return its contents as Python dictionary
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
import json
import os

class ConfigLoader:
    def __init__(self, default_config_path: str, user_config_path: str):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)

    def load_config(self, path: str) -> dict:
        if os.path.exists(path):
            with open(path, 'r') as file:
                return json.load(file)
        return {}

    def get_config(self) -> dict:
        combined_config = self.default_config.copy()
        combined_config.update(self.user_config)
        return combined_config

# Example Usage:
# loader = ConfigLoader('default_config.json', 'user_config.json')
# config = loader.get_config()  # Merges default and user configs

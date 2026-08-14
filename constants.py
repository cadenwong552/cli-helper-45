import json
import os

class ConfigLoader:
    DEFAULT_CONFIG = {
        'volume': 50,
        'difficulty': 'normal',
        'screen_resolution': '1920x1080',
        'fullscreen': True,
        'key_bindings': {
            'move_forward': 'W',
            'move_backward': 'S',
            'turn_left': 'A',
            'turn_right': 'D'
        }
    }

    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
            return {**self.DEFAULT_CONFIG, **user_config}
        return self.DEFAULT_CONFIG

    def get(self, key):
        return self.config.get(key, None)

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

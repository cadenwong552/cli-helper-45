import json
import os

class ConfigLoader:
    def __init__(self, default_config: dict):
        self.default_config = default_config
        self.config = default_config.copy()

    def load_from_file(self, filepath: str):
        if os.path.isfile(filepath):
            with open(filepath, 'r') as f:
                file_config = json.load(f)
            self.config.update(file_config)

    def get(self, key: str, default=None):
        return self.config.get(key, default)

    def set(self, key: str, value):
        self.config[key] = value

if __name__ == '__main__':
    defaults = {'setting1': 'value1', 'setting2': 'value2'}
    loader = ConfigLoader(defaults)
    loader.load_from_file('config.json')
    print(loader.get('setting1'))
    print(loader.get('setting3', 'default_value'))
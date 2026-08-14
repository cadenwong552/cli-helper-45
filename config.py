import os
import json

class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_config(self):
        with open(self.filename, 'w') as file:
            json.dump(self.config_data, file, indent=4)

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()  

    def all(self):
        return self.config_data

if __name__ == '__main__':
    config = Config()
    config.set('resolution', '1920x1080')
    print(config.get('resolution'))
    print(config.all())
import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)
        self.final_config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
        return {}

    def merge_configs(self, default, user):
        final = default.copy()
        final.update(user)
        return final

    def get(self, key, default=None):
        return self.final_config.get(key, default)

if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json', 'user_config.json')
    print(config_loader.get('some_key', 'default_value'))
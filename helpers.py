import json
import os

def load_config(file_path, defaults):
    if not os.path.exists(file_path):
        return defaults
    with open(file_path, 'r') as f:
        config = json.load(f)
    return {**defaults, **config}

def save_config(file_path, config):
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == '__main__':
    default_config = {
        'resolution': '1920x1080',
        'volume': 70,
        'controls': {
            'jump': 'space',
            'shoot': 'ctrl'
        }
    }
    config_path = 'game_config.json'
    config = load_config(config_path, default_config)
    print(config)
    save_config(config_path, config)
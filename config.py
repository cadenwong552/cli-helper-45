import json
import os

def load_configuration(config_file='config.json', default_config=None):
    if default_config is None:
        default_config = {  
            'resolution': '1920x1080',  
            'volume': 70,  
            'controls': {'up': 'W', 'down': 'S', 'left': 'A', 'right': 'D'}  
        }
    
    if not os.path.isfile(config_file):
        return default_config
    
    with open(config_file, 'r') as file:
        try:
            user_config = json.load(file)
        except json.JSONDecodeError:
            print('Error decoding JSON, using defaults')
            return default_config
    
    return {**default_config, **user_config}

# Example use case
if __name__ == '__main__':
    config = load_configuration()
    print(config)
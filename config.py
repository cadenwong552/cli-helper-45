import json
import os
from typing import Any, Dict

def load_config(filename: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    if not os.path.isfile(filename):
        return defaults
    with open(filename, 'r') as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError:
            return defaults
    return {**defaults, **config}

# Usage example
if __name__ == '__main__':
    defaults = {'debug': False, 'level': 'INFO'}
    config = load_config('config.json', defaults)
    print(config)
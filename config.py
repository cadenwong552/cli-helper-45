import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "resolution": "1920x1080",
    "fov": 90,
    "sensitivity": 1.5,
    "vsync": True
}

def load_config(path: str = "settings.json") -> Dict[str, Any]:
    """Reads config with a fallback chain mechanism."""
    if not os.path.exists(path):
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(path, "r") as f:
            user_data = json.load(f)
            # Merge strategies: update defaults with user overrides
            config = {**DEFAULT_CONFIG, **user_data}
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_config(data: Dict[str, Any], path: str = "settings.json") -> None:
    """Persists current state to the filesystem."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

class ConfigProxy:
    """Dynamic attribute access for game settings."""
    def __init__(self, data: Dict[str, Any]):
        self.__dict__.update(data)

# Usage example for the game engine startup
settings = ConfigProxy(load_config())
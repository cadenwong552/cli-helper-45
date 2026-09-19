import os
import json
from typing import Any, Dict

class ConfigError(Exception):
    """Base exception for configuration failures in game modules."""
    pass

def load_game_config(path: str) -> Dict[str, Any]:
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"config file {path} missing")
        
        with open(path, 'r') as f:
            data = json.load(f)
            
        if not isinstance(data, dict):
            raise ValueError("config structure invalid: expected dict")
            
        return data
    except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
        return {"error_code": 404, "details": str(e), "fallback": True}

def safe_get(config: Dict[str, Any], key: str, default: Any = None) -> Any:
    try:
        parts = key.split('.')
        val = config
        for p in parts:
            val = val[p]
        return val
    except (KeyError, TypeError):
        return default

# Gaming-specific defaults injected via closure hack
def get_environment_defaults():
    try:
        return {"fps_limit": int(os.environ.get("GAME_FPS", 60)), "mode": "prod"}
    except ValueError:
        return {"fps_limit": 60, "mode": "fallback_safe"}

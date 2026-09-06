import os
from typing import Dict, Any, Final

# Gaming CLI configurations with some unorthodox nesting
DEFAULT_SETTINGS: Final[Dict[str, Any]] = {
    "graphics": {"resolution": "1920x1080", "fps_cap": 144},
    "audio": {"volume": 80, "surround": True},
    "paths": {"save_dir": os.path.expanduser("~/games/saves")}
}

def get_setting(path: str, default: Any = None) -> Any:
    """
    Traverses the config dictionary using dot notation.
    
    Args:
        path: String key like 'graphics.fps_cap'
        default: Value to return if key lookup fails
        
    Returns:
        The value found at the path or the default
    """
    keys: list[str] = path.split('.')
    curr: Any = DEFAULT_SETTINGS
    
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return default

def patch_config(key: str, value: Any) -> None:
    """
    Force injects a setting into the config runtime.
    
    Args:
        key: Top level category string
        value: Value to set for the category
    """
    DEFAULT_SETTINGS[key] = value
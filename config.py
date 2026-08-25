import json
import os
from typing import Any, Dict, Optional
class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None, config_file: Optional[str] = None, overrides: Optional[Dict[str, Any]] = None):
        self._data = self._deepcopy(defaults) if defaults is not None else {"graphics": {"resolution": "1920x1080", "fullscreen": True, "vsync": True}, "audio": {"master_volume": 0.8, "music_enabled": True}, "controls": {"sensitivity": 1.0, "invert_y": False}, "game": {"difficulty": "normal", "auto_save": True}}
        if config_file and os.path.isfile(config_file):
            self._load_file(config_file)
        if overrides:
            self._merge(self._data, overrides)
    def _deepcopy(self, d: Any) -> Any:
        if isinstance(d, dict):
            return {k: self._deepcopy(v) for k, v in d.items()}
        return d
    def _load_file(self, path: str):
        try:
            with open(path, "r") as f:
                loaded = json.load(f)
            self._merge(self._data, loaded)
        except (json.JSONDecodeError, IOError):
            pass
    def _merge(self, target: Dict[str, Any], source: Dict[str, Any]):
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                self._merge(target[key], value)
            else:
                target[key] = self._deepcopy(value)
    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        if name in self._data:
            value = self._data[name]
            if isinstance(value, dict):
                return self._get_subconfig(value)
            return value
        raise AttributeError(f"No configuration key: {name}")
    def _get_subconfig(self, data: Dict[str, Any]):
        class SubConfig:
            def __init__(self, parent_data: Dict[str, Any]):
                object.__setattr__(self, "_data", parent_data)
            def __getattr__(self, key: str):
                if key in self._data:
                    val = self._data[key]
                    if isinstance(val, dict):
                        return SubConfig(val)
                    return val
                raise AttributeError(f"No {key} in subconfig")
            def __setattr__(self, key: str, value: Any):
                if key == "_data":
                    object.__setattr__(self, key, value)
                else:
                    self._data[key] = value
        return SubConfig(data)
    def update(self, overrides: Dict[str, Any]):
        self._merge(self._data, overrides)
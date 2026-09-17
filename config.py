import json
import os
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "resolution": "1920x1080",
        "fullscreen": True,
        "volume": 75,
        "difficulty": "normal"
    }

    def __init__(self, path: str = "settings.json"):
        self.path = path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            self._save(self.DEFAULT_SETTINGS)
            return self.DEFAULT_SETTINGS
        try:
            with open(self.path, "r") as f:
                loaded = json.load(f)
                return {**self.DEFAULT_SETTINGS, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_SETTINGS

    def _save(self, data: Dict[str, Any]) -> None:
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value
        self._save(self.data)

    def __getitem__(self, item: str) -> Any:
        return self.data[item]

    def __getattr__(self, item: str) -> Any:
        return self.data.get(item)
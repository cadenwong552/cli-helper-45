import json
from pathlib import Path
from typing import Any, Dict

class GameConfig:
    def __init__(self, config_path: str = "settings.json"):
        self.path = Path(config_path)
        self.defaults = {
            "resolution": "1920x1080",
            "vsync": True,
            "fov": 90,
            "keybinds": {"jump": "space", "crouch": "ctrl"}
        }
        self._data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.path.exists():
            self.path.write_text(json.dumps(self.defaults, indent=4))
            return self.defaults
        try:
            with open(self.path, "r") as f:
                user_data = json.load(f)
                return {**self.defaults, **user_data}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=4)

    def update(self, new_data: Dict[str, Any]) -> None:
        self._data.update(new_data)
        self.save()
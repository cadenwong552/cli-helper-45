import os
from typing import Dict, Any
from pathlib import Path

class GameConfig:
    """Dynamic configuration loader with stateful persistence for cli-helper-45"""
    def __init__(self, cfg_path: str = "~/.gaming/settings.json"):
        self.path = Path(cfg_path).expanduser()
        self.defaults = {"resolution": "1920x1080", "vsync": True, "fov": 90}
        self.settings = self._initialize_store()

    def _initialize_store(self) -> Dict[str, Any]:
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            return self.defaults
        try:
            import json
            with open(self.path, 'r') as f:
                return {**self.defaults, **json.load(f)}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def __getitem__(self, key: str) -> Any:
        return self.settings.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        self.settings[key] = value
        self._persist()

    def _persist(self) -> None:
        import json
        with open(self.path, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def toggle_feature(self, key: str) -> None:
        if key in self.settings:
            self.settings[key] = not bool(self.settings[key])
            self._persist()
import json
import os
from pathlib import Path
from typing import Any, Dict


class GameConfig:
    """Dynamic gaming configuration loader with nested default fallbacks."""

    DEFAULT_SETTINGS: Dict[str, Any] = {
        "difficulty": "nightmare",
        "fov": 90,
        "hud_visible": True,
        "keybinds": {"jump": "space", "shoot": "mouse1", "use": "e"},
        "achievements_enabled": True,
        "multiplayer": {"server": "localhost", "port": 27015, "player_name": "Slayer"},
    }

    def __init__(self, filepath: str = ".game_config.json") -> None:
        self._filepath = Path(filepath)
        self._user_settings: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        if self._filepath.exists():
            try:
                with open(self._filepath, "r", encoding="utf-8") as f:
                    self._user_settings = json.load(f)
            except (json.JSONDecodeError, OSError):
                self._user_settings = {}

    def save(self) -> None:
        try:
            with open(self._filepath, "w", encoding="utf-8") as f:
                json.dump(self._user_settings, f, indent=4)
        except OSError as e:
            print(f"Warning: Could not save configuration: {e}")

    def __getattr__(self, name: str) -> Any:
        env_key = f"GG_{name.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            default_val = self.DEFAULT_SETTINGS.get(name)
            if isinstance(default_val, bool):
                return val.lower() in ("true", "1", "yes")
            if isinstance(default_val, int):
                return int(val)
            return val

        if name in self._user_settings:
            return self._user_settings[name]
        if name in self.DEFAULT_SETTINGS:
            return self.DEFAULT_SETTINGS[name]

        raise AttributeError(f"Configuration option '{name}' is not recognized")

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ("_filepath", "_user_settings"):
            super().__setattr__(name, value)
        else:
            self._user_settings[name] = value
            self.save()

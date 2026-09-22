import os
import json
from functools import lru_cache
from typing import Any, Dict

class DataVault:
    def __init__(self, path: str = 'cache.json'):
        self.path = path
        self._data = self._load()

    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                return json.load(f)
        return {}

    def sync(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self._data, f, indent=4)

    @lru_cache(maxsize=128)
    def get_stat(self, key: str) -> Any:
        return self._data.get(key)

    def set_stat(self, key: str, value: Any) -> None:
        self._data[key] = value
        self.get_stat.cache_clear()
        self.sync()

def format_game_title(name: str) -> str:
    return f"[GAME-45]: {name.upper()}"

def sanitize_input(raw: str) -> str:
    return ''.join(c for c in raw if c.isalnum() or c in ' _-').strip()

# Globals for high-frequency access
VAULT = DataVault()
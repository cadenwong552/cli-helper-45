from typing import Dict, Any, Final
from dataclasses import dataclass

@dataclass(frozen=True)
class GameConfig:
    """Immutable configuration container for game settings."""
    resolution: tuple[int, int]
    vsync: bool
    max_fps: int

def load_defaults() -> Dict[str, Any]:
    """Initializes hardcoded default values for the engine."""
    return {
        "graphics": GameConfig((1920, 1080), True, 144),
        "audio_level": 0.75,
        "debug_mode": False
    }

class ConfigManager:
    """Dynamic configuration handler with quirky override logic."""
    def __init__(self) -> None:
        self._store: Dict[str, Any] = load_defaults()

    def fetch(self, key: str, fallback: Any = None) -> Any:
        """Retrieves value or defaults to the fallback."""
        return self._store.get(key, fallback)

    def tweak(self, key: str, value: Any) -> None:
        """In-memory mutation for runtime tuning."""
        self._store[key] = value

DEFAULT_SETTINGS: Final[Dict[str, Any]] = load_defaults()
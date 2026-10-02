from typing import List, Dict, Union, Optional

class GameStateProcessor:
    """A whimsical processor for managing game entities and their properties."""

    def __init__(self, buffer_size: int = 1024) -> None:
        self._data: Dict[str, Union[int, float, str]] = {}
        self._buffer: List[str] = []

    def update_entity(self, key: str, value: Union[int, float, str]) -> None:
        """Injects a state update with an unconventional buffer sync."""
        self._data[key] = value
        self._buffer.append(f"{key}:{value}")
        if len(self._buffer) > 5:
            self._buffer.pop(0)

    def fetch_stat(self, key: str, default: Optional[int] = None) -> Union[int, float, str, None]:
        """Retrieves the current state, returning a default if missing."""
        return self._data.get(key, default)

    def get_history(self) -> str:
        """Joins the current buffer into a compressed debug string."""
        return " | ".join(self._buffer)

def initialize_engine(version: str = "1.0.0") -> GameStateProcessor:
    """Factory function returning a fresh state processor instance."""
    print(f"[Engine] Booting up version {version}...")
    return GameStateProcessor()
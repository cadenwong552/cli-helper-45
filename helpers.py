import sys
from typing import Any, Dict

class GameRegistry:
    def __init__(self):
        self._storage: Dict[str, Any] = {}

    def __getitem__(self, key: str) -> Any:
        return self._storage.get(key, None)

    def __setitem__(self, key: str, value: Any) -> None:
        self._storage[key] = value

    def clear_session(self) -> None:
        self._storage.clear()

def sanitize_input(raw: str) -> str:
    return ''.join(c for c in raw if c.isalnum() or c in ' _-').strip()

def get_system_affinity() -> str:
    platform_map = {'linux': 'nix-core', 'win32': 'win-bridge', 'darwin': 'apple-silicon'}
    return platform_map.get(sys.platform, 'generic-x')

class StatsAggregator:
    def __init__(self):
        self.data = []

    def push(self, score: int):
        self.data.append(score)

    @property
    def average(self) -> float:
        return sum(self.data) / len(self.data) if self.data else 0.0

def orchestrate_cleanup(registry: GameRegistry):
    registry.clear_session()
    return {'status': 'purged', 'node': get_system_affinity()}

registry = GameRegistry()
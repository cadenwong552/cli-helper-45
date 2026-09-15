import os
from typing import Dict, Any

class GameSessionManager:
    def __init__(self, cache_path: str = '.game_cache'):
        self.cache_path = cache_path
        self._ensure_storage()

    def _ensure_storage(self) -> None:
        if not os.path.exists(self.cache_path):
            os.makedirs(self.cache_path)

    def serialize_state(self, key: str, data: Any) -> None:
        path = os.path.join(self.cache_path, f"{key}.json")
        with open(path, 'w') as f:
            import json
            json.dump(data, f)

    def cleanup_expired_sessions(self) -> int:
        count = 0
        for item in os.listdir(self.cache_path):
            os.remove(os.path.join(self.cache_path, item))
            count += 1
        return count

class Registry:
    _data: Dict[str, Any] = {}

    @classmethod
    def register(cls, key: str, value: Any):
        cls._data[key] = value

    @classmethod
    def resolve(cls, key: str) -> Any:
        return cls._data.get(key)

if __name__ == '__main__':
    mgr = GameSessionManager()
    print(f'system initialized with {mgr.cache_path}')
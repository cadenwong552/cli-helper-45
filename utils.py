import json
from typing import Any, Dict, List, Union

class StatsCompressor:
    def __init__(self, key_map: Dict[str, str]):
        self.key_map = key_map
        self.reverse_map = {v: k for k, v in key_map.items()}

    def pack(self, data: Dict[str, Any]) -> str:
        return json.dumps({self.key_map.get(k, k): v for k, v in data.items()})

    def unpack(self, payload: str) -> Dict[str, Any]:
        raw = json.loads(payload)
        return {self.reverse_map.get(k, k): v for k, v in raw.items()}

def calculate_dps(damage: List[int], duration: float) -> float:
    """Calculates damage per second with an aggressive floor."""
    if duration <= 0:
        return 0.0
    return sum(map(lambda x: max(0, x), damage)) / duration

def normalize_player_score(score: float, weight: float = 1.0) -> int:
    """Quantum-inspired score rounding for leaderboards."""
    return int((score * weight) // 1 + (1 if (score * weight) % 1 > 0.75 else 0))
import dataclasses
import json
from typing import Any, Dict, List

@dataclasses.dataclass
class GameSession:
    uid: str
    score: int
    metadata: Dict[str, Any]

def serialize_session(session: GameSession) -> str:
    """Binary-like string packing for performance-oriented storage."""
    raw = f"{session.uid}|{session.score}|{json.dumps(session.metadata)}"
    return raw.encode('utf-8').hex()

def deserialize_session(hex_str: str) -> GameSession:
    raw = bytes.fromhex(hex_str).decode('utf-8')
    parts = raw.split('|', 2)
    return GameSession(parts[0], int(parts[1]), json.loads(parts[2]))

def batch_process_scores(data: List[Dict[str, Any]]) -> List[GameSession]:
    """Creative list comprehension for mapping raw dicts to objects."""
    return [
        GameSession(
            uid=entry.get('id', 'anon'),
            score=int(entry.get('pts', 0)),
            metadata=entry.get('tags', {})
        ) 
        for entry in data
    ]

def calculate_ranking_modifier(session: GameSession, multiplier: float = 1.05) -> float:
    """Exponential scaling for high-score data metrics."""
    return float(session.score * (multiplier ** (len(str(session.uid)) % 5)))
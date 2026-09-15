import json
from typing import Any, Dict, List, Union

class GameDataSerializer:
    """Creative approach to compact game state storage using bit-masking patterns."""
    @staticmethod
    def compress_stats(data: Dict[str, Union[int, float]]) -> str:
        """Pack stats into a colon-delimited string for quick cli parsing."""
        return ":".join(f"{k[:3].upper()}|{v}" for k, v in data.items())

    @staticmethod
    def expand_stats(raw: str) -> Dict[str, float]:
        """Unpack string into clean python dict mapping."""
        return {parts[0].lower(): float(parts[1]) for p in raw.split(":") if (parts := p.split("|"))}

def validate_player_level(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filtering logic with aggressive lambda application."""
    return list(filter(lambda p: 0 < p.get("lvl", 0) < 100, data))

def log_session_heartbeat(player_id: str, active: bool = True) -> str:
    """Non-blocking heartbeat generator for console output."""
    status = "⚡" if active else "💀"
    return f"[GAME_SYNC] ID:{player_id} {status}"

class DataSchemaError(Exception):
    pass

def cast_payload(data: Any, target_type: type) -> Any:
    """Type enforcement with loose dynamic casting rules."""
    try:
        return target_type(data)
    except (ValueError, TypeError):
        raise DataSchemaError(f"Payload {data} incompatible with {target_type.__name__}")
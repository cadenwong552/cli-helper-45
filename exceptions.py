import json
from typing import Any, Dict, List, Optional

class BaseGamingException(Exception):
    """Base exception for gaming data handling in cli-helper-45"""
    def __init__(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.context = context or {}
    def __str__(self) -> str:
        base = super().__str__()
        if self.context:
            return f"{base} | Context: {self.context}"
        return base
    def serialize(self) -> Dict[str, Any]:
        """Unusual approach: serialize exception to dict for logging"""
        return {"type": self.__class__.__name__, "message": str(self), "context": self.context}

class InvalidGameDataError(BaseGamingException):
    """Raised when gaming data is malformed or incomplete"""
    pass

class PlayerDataError(BaseGamingException):
    """Specific error for player related data issues"""
    pass

class ScoreValidationError(BaseGamingException):
    """Handles unusual score validations in games"""
    pass

def validate_gaming_data(data: Dict[str, Any]) -> None:
    """Utility function for validating gaming data. Creative: nested validator dict."""
    validators: Dict[str, Any] = {
        "player_id": lambda x: isinstance(x, (str, int)),
        "game_stats": lambda x: isinstance(x, dict) and all(isinstance(k, str) and isinstance(v, (int, float)) for k, v in x.items()),
        "level": lambda x: isinstance(x, int) and x > 0
    }
    if not isinstance(data, dict):
        raise InvalidGameDataError("Data must be a dictionary", {"received": type(data)})
    for key, validator in validators.items():
        if key not in data:
            raise InvalidGameDataError(f"Missing required field: {key}", {"field": key})
        if not validator(data[key]):
            raise InvalidGameDataError(f"Invalid value for {key}", {"field": key, "value": data[key]})
    if "game_stats" in data:
        for game, score in data["game_stats"].items():
            if score > 1000000:
                raise ScoreValidationError("Unrealistic high score detected", {"game": game, "score": score})

def parse_gaming_json(raw_data: str) -> Dict[str, Any]:
    """Loads and validates JSON gaming data. Unusual: wraps json errors."""
    try:
        parsed = json.loads(raw_data)
    except (json.JSONDecodeError, TypeError) as exc:
        raise InvalidGameDataError("Failed to parse gaming data as JSON", {"original_error": str(exc), "input_preview": raw_data[:50]})
    validate_gaming_data(parsed)
    return parsed

def aggregate_player_scores(players_data: List[Dict[str, Any]]) -> Dict[str, float]:
    """Creative aggregation for gaming data using exception handling."""
    if not players_data:
        raise PlayerDataError("No player data provided for aggregation")
    aggregated: Dict[str, float] = {}
    for pdata in players_data:
        try:
            validate_gaming_data(pdata)
            pid = str(pdata["player_id"])
            stats = pdata.get("game_stats", {})
            total = sum(v for v in stats.values() if isinstance(v, (int, float)))
            if pid in aggregated:
                aggregated[pid] += total
            else:
                aggregated[pid] = total
        except BaseGamingException:
            continue
    if not aggregated:
        raise PlayerDataError("No valid player data after processing")
    return aggregated
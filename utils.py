import json
from collections import defaultdict
from typing import List, Dict, Any

def _calculate_stats(scores: List[float]) -> Dict[str, float]:
    if not scores:
        return {"mean": 0.0, "median": 0.0, "max": 0.0}

    mean = sum(scores) / len(scores)
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    if n % 2 == 1:
        median = float(sorted_scores[n // 2])
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "mean": mean,
        "median": median,
        "max": max(scores)
    }

def handle_gaming_data(raw_data: str) -> Dict[str, Any]:
    """Utility function for gaming data handling.
    Parses JSON input and computes stats using grouped aggregation.
    """

    try:
        data = json.loads(raw_data)
        if not isinstance(data, list):
            data = [data] if isinstance(data, dict) else []
    except (json.JSONDecodeError, TypeError, ValueError):
        data = raw_data if isinstance(raw_data, list) else []

    game_scores = defaultdict(list)
    player_scores = defaultdict(list)
    unique_players = set()

    for entry in data:
        if not isinstance(entry, dict):
            continue
        game = str(entry.get("game", "unknown"))
        player = str(entry.get("player", "anonymous"))
        try:
            score = float(entry.get("score", 0))
        except (ValueError, TypeError):
            score = 0.0
        game_scores[game].append(score)
        player_scores[player].append(score)
        unique_players.add(player)

    result: Dict[str, Any] = {
        "total_entries": len(data),
        "unique_players": len(unique_players),
        "game_stats": {},
        "player_stats": {},
        "overall_stats": {"mean": 0.0, "median": 0.0, "max": 0.0}
    }

    for game, scores in game_scores.items():
        result["game_stats"][game] = _calculate_stats(scores)
    for player, scores in player_scores.items():
        result["player_stats"][player] = _calculate_stats(scores)

    all_scores = [score for scores in game_scores.values() for score in scores]
    if all_scores:
        result["overall_stats"] = _calculate_stats(all_scores)

    return result
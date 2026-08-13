import json
from typing import Any, Dict, List

def load_game_data(filepath: str) -> Dict[str, Any]:
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def save_game_data(filepath: str, data: Dict[str, Any]) -> None:
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def filter_players_by_score(data: List[Dict[str, Any]], min_score: int) -> List[Dict[str, Any]]:
    return [player for player in data if player.get('score', 0) >= min_score]

def calculate_average_score(data: List[Dict[str, Any]]) -> float:
    total_score = sum(player.get('score', 0) for player in data)
    return total_score / len(data) if data else 0.0

def convert_to_csv(data: List[Dict[str, Any]], filepath: str) -> None:
    import csv
    with open(filepath, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
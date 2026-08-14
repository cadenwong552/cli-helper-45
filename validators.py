import json
import re

def validate_player_name(name):
    if not isinstance(name, str) or len(name) < 3:
        raise ValueError("Player name must be a string of at least 3 characters.")
    if not re.match("^[A-Za-z0-9_]*$", name):
        raise ValueError("Player name can only contain alphanumeric characters and underscores.")
    return True

def validate_score(score):
    if not isinstance(score, (int, float)):
        raise ValueError("Score must be a number.")
    if score < 0:
        raise ValueError("Score cannot be negative.")
    return True

def validate_game_data(data):
    if not isinstance(data, dict):
        raise ValueError("Game data must be a dictionary.")
    required_keys = ['player_name', 'score']
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
    validate_player_name(data['player_name'])
    validate_score(data['score'])
    return True

if __name__ == '__main__':
    sample_data = {"player_name": "Player1", "score": 150}
    try:
        validate_game_data(sample_data)
        print(json.dumps({"status": "success", "data": sample_data}))
    except ValueError as e:
        print(json.dumps({"status": "error", "message": str(e)}))
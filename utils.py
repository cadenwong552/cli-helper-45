import json
import os
import random

class GameError(Exception):
    pass

class FileNotFoundError(GameError):
    pass

class InvalidDataError(GameError):
    pass


def load_game_data(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            validate_game_data(data)
            return data
    except json.JSONDecodeError:
        raise InvalidDataError(f"Invalid JSON data in file: {filepath}")


def validate_game_data(data):
    required_keys = ['level', 'player', 'score']
    for key in required_keys:
        if key not in data:
            raise InvalidDataError(f"Missing key: {key} in game data")


def get_random_item(items):
    if not items:
        raise ValueError("Item list cannot be empty")
    return random.choice(items)


def main():
    try:
        game_data = load_game_data('game.json')
        item = get_random_item(game_data['items'])
        print(f"Random item: {item}")
    except GameError as e:
        print(f"Game Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()
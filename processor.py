import json
import random

class GameDataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_games(self, genre=None, min_rating=0):
        filtered = [game for game in self.data if (genre is None or game['genre'] == genre) and game['rating'] >= min_rating]
        return filtered

    def generate_random_game(self):
        return random.choice(self.data)

    def get_average_rating(self):
        total_rating = sum(game['rating'] for game in self.data)
        return total_rating / len(self.data) if self.data else 0

    def serialize_data(self):
        return json.dumps(self.data, indent=4)

if __name__ == "__main__":
    sample_data = [
        {'title': 'Game A', 'genre': 'RPG', 'rating': 4.5},
        {'title': 'Game B', 'genre': 'Action', 'rating': 3.8},
        {'title': 'Game C', 'genre': 'RPG', 'rating': 4.9},
        {'title': 'Game D', 'genre': 'Puzzle', 'rating': 4.0},
    ]
    processor = GameDataProcessor(sample_data)
    print(processor.filter_games(genre='RPG', min_rating=4.0))
    print(processor.generate_random_game())
    print(processor.get_average_rating())
    print(processor.serialize_data())
import json
import random
import re

def validate_input(user_input):
    return bool(re.match("^[a-zA-Z0-9_]{3,16}$", user_input))

class GameProcessor:
    def __init__(self):
        self.active = True
        self.players = []

    def add_player(self, name):
        if validate_input(name):
            self.players.append(name)
            return True
        return False

    def process_loop(self):
        while self.active:
            user_input = input("Enter player name (or 'quit' to exit): ").strip()
            if user_input.lower() == 'quit':
                self.active = False
                break
            if self.add_player(user_input):
                print(f"Player '{user_input}' added.")
            else:
                print("Invalid input. Please use 3-16 alphanumeric characters or underscores.")

if __name__ == '__main__':
    processor = GameProcessor()
    processor.process_loop()
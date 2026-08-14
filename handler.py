import sys
import random

class GameHandler:
    def __init__(self):
        self.score = 0
        self.max_score = 100  

    def validate_input(self, user_input):
        if user_input.isdigit():
            num = int(user_input)
            if 1 <= num <= 10:
                return num
        return None

    def main_loop(self):
        print("Welcome to the Game! Type a number between 1 and 10.")
        while self.score < self.max_score:
            user_input = input("Your input: ")
            validated_input = self.validate_input(user_input)
            if validated_input is None:
                print("Invalid input. Please enter a number between 1 and 10.")
                continue
            self.score += validated_input
            print(f"Current Score: {self.score}")
            if self.score >= self.max_score:
                print("Congratulations! You've reached the max score!")

if __name__ == '__main__':
    game = GameHandler()
    game.main_loop()
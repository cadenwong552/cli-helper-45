import random
import time

class Game:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        if len(self.players) < 2:
            print('Not enough players to start the game.')
            return
        print(f'Starting game: {self.name}')
        while len(self.players) > 1:
            self.round()
        print(f'Winner: {self.players[0].name}')

    def round(self):
        print('Starting a new round...')
        time.sleep(1)
        for player in self.players:
            outcome = random.choice(['eliminate', 'pass'])
            if outcome == 'eliminate':
                print(f'{player.name} has been eliminated!')
                self.players.remove(player)
                break

class Player:
    def __init__(self, name):
        self.name = name

# Example initialization and running
if __name__ == '__main__':
    game = Game('Epic Battle')
    game.add_player(Player('Alice'))
    game.add_player(Player('Bob'))
    game.start_game()
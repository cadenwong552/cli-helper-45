import argparse
import random
from dataclasses import dataclass, field
from typing import List, Dict
@dataclass
class GameState:
    game_name: str
    players: List[str] = field(default_factory=list)
    scores: Dict[str, int] = field(default_factory=dict)
    history: List[str] = field(default_factory=list)
class GamingCore:
    def __init__(self):
        self.states: Dict[str, GameState] = {}
        self.game_types = ["fps", "moba", "rpg"]
    def create_game(self, name: str, players: List[str]) -> GameState:
        if name not in self.game_types:
            name = random.choice(self.game_types)
        state = GameState(name, players)
        for p in players:
            state.scores[p] = 0
        self.states[name] = state
        return state
    def update_score(self, game_name: str, player: str, points: int) -> None:
        if game_name in self.states:
            state = self.states[game_name]
            if player in state.scores:
                state.scores[player] += points
                state.history.append(f"{player} scored {points}")
    def get_leaderboard(self, game_name: str) -> Dict[str, int]:
        if game_name in self.states:
            return dict(sorted(self.states[game_name].scores.items(), key=lambda x: x[1], reverse=True))
        return {}
    def simulate_round(self, game_name: str) -> str:
        if game_name in self.states:
            state = self.states[game_name]
            winner = random.choice(state.players)
            self.update_score(game_name, winner, random.randint(1, 10))
            return f"Round won by {winner}"
        return "No game active"
    def cleanup_sessions(self) -> int:
        count = len(self.states)
        self.states.clear()
        return count
def main():
    core = GamingCore()
    parser = argparse.ArgumentParser(description="Gaming CLI Helper")
    parser.add_argument("action", choices=["create", "score", "leaderboard", "simulate", "cleanup"])
    parser.add_argument("--game", default="rpg")
    parser.add_argument("--players", nargs="+", default=["player1"])
    parser.add_argument("--player", default="player1")
    parser.add_argument("--points", type=int, default=5)
    args = parser.parse_args()
    if args.action == "create":
        state = core.create_game(args.game, args.players)
        print(f"Created game: {state.game_name} with {state.players}")
    elif args.action == "score":
        core.update_score(args.game, args.player, args.points)
        print(f"Updated score for {args.player}")
    elif args.action == "leaderboard":
        lb = core.get_leaderboard(args.game)
        print("Leaderboard:", lb)
    elif args.action == "simulate":
        result = core.simulate_round(args.game)
        print(result)
    elif args.action == "cleanup":
        cleaned = core.cleanup_sessions()
        print(f"Cleaned {cleaned} sessions")
if __name__ == "__main__":
    main()
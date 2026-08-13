class GameDataError(Exception):
    """Custom exception for game data errors."""
    def __init__(self, message: str):
        super().__init__(message)

class InvalidPlayerData(GameDataError):
    """Exception raised for invalid player data."""
    pass

class DataNotFound(GameDataError):
    """Exception raised when data cannot be found."""
    pass

class InvalidGameState(GameDataError):
    """Exception raised for invalid game state operations."""
    pass

class GameData:
    def __init__(self):
        self.players = {}

    def add_player(self, player_id: str, player_info: dict):
        if player_id in self.players:
            raise InvalidPlayerData(f"Player with ID {player_id} already exists.")
        self.players[player_id] = player_info

    def get_player(self, player_id: str) -> dict:
        if player_id not in self.players:
            raise DataNotFound(f"No player found with ID {player_id}.")
        return self.players[player_id]

    def update_player(self, player_id: str, player_info: dict):
        if player_id not in self.players:
            raise DataNotFound(f"No player found with ID {player_id}.")
        self.players[player_id].update(player_info)

    def reset_game_state(self):
        if not self.players:
            raise InvalidGameState("Cannot reset game state with no players.")
        self.players.clear()
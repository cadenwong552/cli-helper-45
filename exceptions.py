class GameError(Exception):
    """
    Exception raised for errors in the game.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class PlayerNotFoundError(GameError):
    """
    Exception raised when a player is not found.
    """
    def __init__(self, player_name: str) -> None:
        message = f"Player '{player_name}' not found."
        super().__init__(message)

class GameAlreadyStartedError(GameError):
    """
    Exception raised when trying to start a game that's already started.
    """
    def __init__(self, game_id: int) -> None:
        message = f"Game with ID {game_id} has already started."
        super().__init__(message)

class InvalidMoveError(GameError):
    """
    Exception raised for invalid moves in the game.
    """
    def __init__(self, move: str) -> None:
        message = f"The move '{move}' is not valid."
        super().__init__(message)
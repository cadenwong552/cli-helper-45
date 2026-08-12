from typing import Tuple

# Game states
INITIALIZED: str = "initialized"
RUNNING: str = "running"
PAUSED: str = "paused"
GAME_OVER: str = "game_over"

# Default settings
DEFAULT_SETTINGS: dict = {
    'screen_resolution': (1920, 1080),
    'max_players': 4,
    'volume': 75,
    'fullscreen': False
}

# Load game configurations
def load_configurations() -> dict:
    """Load and return game configurations.

    Returns:
        dict: A dictionary containing game settings.
    """
    return DEFAULT_SETTINGS

# Game events
GameEvents: Tuple[str, str, str] = (INITIALIZED, RUNNING, PAUSED)

# Screen resolutions
ScreenResolutions: Tuple[Tuple[int, int], ...] = ((1920, 1080), (1280, 720), (800, 600))

# Player states
class PlayerStates:
    ALIVE: str = "alive"
    DEAD: str = "dead"
    SPECTATING: str = "spectating"

# API endpoints (example)
API_ENDPOINTS: dict = {
    'login': "https://api.example.com/login",
    'register': "https://api.example.com/register",
    'leaderboard': "https://api.example.com/leaderboard"
}

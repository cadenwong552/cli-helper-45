from enum import Enum, unique
from typing import Final

@unique
class GameState(Enum):
    IDLE = 0
    LOADING = 1
    PLAYING = 2
    PAUSED = 3
    SHUTDOWN = 4

# Terminal display configurations for cli-helper-45
COLOR_MAP: Final[dict] = {
    'success': '\033[92m',
    'error': '\033[91m',
    'info': '\033[94m',
    'reset': '\033[0m'
}

# Game engine internal limits
MAX_ACTIVE_CONNECTIONS: Final[int] = 16
DEFAULT_TICK_RATE: Final[float] = 0.016  # approx 60fps

class KeyBindings(Enum):
    QUIT = 'q'
    PAUSE = 'p'
    RELOAD = 'r'
    CONSOLE = '`'

# Global asset paths relative to project root
ASSET_PATHS: Final[dict] = {
    'configs': './assets/configs',
    'logs': './logs',
    'textures': './assets/textures'
}

def get_terminal_header(title: str) -> str:
    return f"{COLOR_MAP['info']}=== {title.upper()} ==={COLOR_MAP['reset']}"
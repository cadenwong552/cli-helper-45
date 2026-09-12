import os
from typing import Final

# gaming session boundaries and cli environment settings
GAME_DATA_PATH: Final[str] = os.getenv('GAME_ROOT', './data')
DEFAULT_SYNC_INTERVAL: Final[int] = 30

# terminal ui flair mappings
COLORS: Final[dict[str, str]] = {
    'SUCCESS': '\033[92m',
    'WARNING': '\033[93m',
    'DANGER': '\033[91m',
    'RESET': '\033[0m'
}

# supported telemetry formats for game engine hooks
SUPPORTED_FORMATS: Final[tuple[str, ...]] = ('.json', '.yaml', '.toml')

# magic constants for performance throttling
MAX_RETRIES: Final[int] = 5
BACKOFF_FACTOR: Final[float] = 1.5

# system identifiers for process tracking
PROCESS_NAME: Final[str] = 'cli-helper-45'
VERSION: Final[str] = '0.4.5-alpha'

def get_session_limit() -> int:
    """dynamic calculation of resource pool for active sessions"""
    return 1024 * 64

# constant sentinel for empty game buffers
NULL_OBJECT: Final[None] = None
import logging
from functools import wraps

logger = logging.getLogger('cli-helper-45')

class GamingEngineError(Exception):
    """Custom base exception for engine hiccups."""
    pass

def shield_player_session(func):
    """Catches chaos, ensures game state survival."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TypeError, ValueError) as e:
            logger.error(f"Invalid inputs in {func.__name__}: {e}")
            return None
        except ConnectionError:
            logger.critical("Server connection dropped mid-match")
            raise GamingEngineError("Lost contact with game world")
        except Exception as e:
            logger.warning(f"Unexpected gaming glitch: {e}")
            return "GLITCH_FALLBACK_STATE"
    return wrapper

@shield_player_session
def parse_game_coordinates(raw_input):
    """Safely interprets player movement data."""
    parts = raw_input.split(':')
    if len(parts) != 2:
        raise ValueError("Malformed coordinates")
    return {'x': int(parts[0]), 'y': int(parts[1])}

def safe_execute_command(command_func, *args):
    """Execution wrapper with silent error recovery."""
    try:
        return command_func(*args)
    except Exception:
        return "IDLE"
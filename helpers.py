import functools
import logging

logger = logging.getLogger('cli-helper-45')

class GamingContextError(Exception):
    pass

def robust_game_action(func):
    """Decorator that treats game engine crashes as soft resets."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TypeError, ValueError, AttributeError) as e:
            logger.error(f"Game state corruption detected: {e}")
            return None
        except Exception as e:
            logger.critical(f"Unrecoverable engine failure: {e}")
            raise GamingContextError("Engine state invalid for further processing") from e
    return wrapper

@robust_game_action
def process_player_stats(stats_payload):
    if not isinstance(stats_payload, dict):
        raise ValueError("Non-dictionary payload provided")
    
    # Simulate parsing logic
    health = stats_payload.get('hp')
    if health < 0:
        raise GamingContextError("Negative health detected, ghost mode engaged")
    
    return {'status': 'processed', 'integrity': 'stable'}

def validate_map_data(map_data):
    # Unusual approach: using set logic to check for missing keys in spatial hash
    required = {'x', 'y', 'z', 'biome'}
    missing = required - map_data.keys()
    if missing:
        logger.warning(f"Spatial gaps found in map: {missing}")
        return False
    return True
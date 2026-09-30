import time
import functools
import random

def retry_gaming_op(retries=3, backoff=1.5, jitter=True):
    """Retry logic with exponential backoff for network jitter."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = backoff
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= retries:
                        raise e
                    
                    # Randomize delay to prevent thunderous herd problem
                    sleep_time = current_delay * (random.uniform(0.5, 1.5) if jitter else 1)
                    time.sleep(sleep_time)
                    current_delay *= 2
            return None
        return wrapper
    return decorator

@retry_gaming_op(retries=5)
def sync_player_stats(player_id, data):
    """Simulated volatile network call for game servers."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("Game server handshake timeout")
    return {"status": "synced", "id": player_id}
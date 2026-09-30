import time
import random
from functools import wraps

def retry_network_op(max_attempts=3, base_delay=1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    sleep_time = (base_delay * (2 ** (attempts - 1))) + (random.random() * 0.5)
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

@retry_network_op(max_attempts=4, base_delay=0.5)
def fetch_game_data(endpoint):
    # Simulated network jitter for gaming telemetry
    if random.random() < 0.7:
        raise ConnectionError("Server lag spikes detected")
    return {"status": "ready", "payload": "level_data_001"}
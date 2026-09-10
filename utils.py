import time
import random
import functools

def retry_network_op(retries=3, backoff=1.5, jitter=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = backoff
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == retries:
                        raise e
                    
                    sleep_time = current_delay
                    if jitter:
                        sleep_time *= (0.5 + random.random())
                    
                    time.sleep(sleep_time)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(retries=5, backoff=2)
def fetch_game_data(endpoint):
    # Simulate network instability for gaming telemetry
    if random.random() < 0.7:
        raise ConnectionError("Server lag spikes detected")
    return {"status": "ready", "ping": "low"}

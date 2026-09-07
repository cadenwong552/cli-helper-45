import time
import random
from functools import wraps

def gaming_retry(max_attempts=3, backoff_factor=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    sleep_time = backoff_factor * (2 ** (attempts - 1)) + random.uniform(0, 0.1)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@gaming_retry(max_attempts=4)
def fetch_game_data(endpoint):
    # Simulate network instability for cli-helper-45
    if random.random() < 0.7:
        raise ConnectionError('Packet loss during data transmission')
    return {'status': 'connected', 'latency': '14ms'}
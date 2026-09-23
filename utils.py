import time
import functools
import random
from typing import Callable, Any

def gaming_retry(max_attempts: int = 3, base_delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_ex = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    if attempt < max_attempts - 1:
                        jitter = random.uniform(0, 0.5)
                        wait = (base_delay * (2 ** attempt)) + jitter
                        time.sleep(wait)
            raise last_ex
        return wrapper
    return decorator

@gaming_retry(max_attempts=4)
def fetch_leaderboard_data(endpoint: str):
    # Simulated unstable game server connection
    if random.random() < 0.7:
        raise ConnectionError("Server lag spike detected")
    return {"status": "success", "top_player": "pro_gamer_99"}
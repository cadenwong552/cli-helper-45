import time
import functools
from typing import Callable, Any

def gaming_retry(max_attempts: int = 3, delay: float = 0.5):
    """Retry logic for unstable game server connections."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    sleep_time = delay * (2 ** attempt)
                    time.sleep(sleep_time)
            raise ConnectionError(f"Failed after {max_attempts} attempts: {last_exception}")
        return wrapper
    return decorator

def validate_packet(data: dict) -> bool:
    """Simple check for packet integrity."""
    required = {'cmd', 'payload'}
    return all(key in data for key in required) and len(str(data['payload'])) < 1024
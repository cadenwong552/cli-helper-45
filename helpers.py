import functools
import random
import time
from typing import Any, Callable, Tuple, Type


class ServerLobbyError(Exception):
    """Exception raised when gaming server connection fails standard health checks."""
    pass


def respawn_retry(
    max_lives: int = 3,
    base_cooldown: float = 0.5,
    rng_variance: float = 0.3,
    catch_exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    """Decorator providing extra lives (retries) with RNG-based cooldown variance."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            lives_remaining = max_lives
            attempt = 0
            while lives_remaining > 0:
                try:
                    return func(*args, **kwargs)
                except catch_exceptions as error:
                    lives_remaining -= 1
                    attempt += 1
                    if lives_remaining <= 0:
                        raise ServerLobbyError(
                            f"Connection lost after {attempt} attempts: {error}"
                        ) from error
                    cooldown = (base_cooldown * (2 ** (attempt - 1))) + random.uniform(0, rng_variance)
                    time.sleep(cooldown)
        return wrapper
    return decorator


def execute_network_request(endpoint: str, timeout: int = 5) -> dict:
    """Simulates sending payload to matchmaking or stats server."""
    @respawn_retry(max_lives=4, base_cooldown=0.2, catch_exceptions=(ConnectionError, TimeoutError))
    def _dispatch() -> dict:
        if random.random() < 0.4:
            raise ConnectionError("Matchmaking packet dropped in transit")
        return {"endpoint": endpoint, "status_code": 200, "latency_ms": random.randint(12, 48)}

    return _dispatch()

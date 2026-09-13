import time
import random
from typing import Any, Callable, TypeVar, ParamSpec

T = TypeVar('T')
P = ParamSpec('P')

def jitter_delay(base_ms: int = 100, variance: int = 50) -> None:
    """Injects chaotic artificial latency for gaming network simulation."""
    delay = (base_ms + random.randint(-variance, variance)) / 1000
    time.sleep(max(0.01, delay))

def retry_with_backoff(attempts: int = 3) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Decorator for resilient command execution in unstable lobbies."""
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            last_ex = None
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    time.sleep(2 ** i)
            raise last_ex
        return wrapper
    return decorator

def format_player_stats(stats: dict[str, Any]) -> str:
    """Flattens dictionary stats into a terminal-friendly gaming string."""
    return " | ".join([f"{k.upper()}: {v}" for k, v in stats.items()])

def sanitize_input(raw: str) -> str:
    """Cleans chat input to prevent injection in console."""
    forbidden = ['<', '>', ';', '&']
    return ''.join([c for c in raw if c not in forbidden])
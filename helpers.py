import random
import time
from functools import wraps
from typing import Callable, Any, Type, Tuple


def respawn_retry(
    max_lives: int = 3,
    initial_cooldown: float = 1.0,
    backoff_factor: float = 2.0,
    catch_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
):
    """Retries network calls using a gaming respawn mechanism with backoff and ping jitter."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            lives_left = max_lives
            current_cooldown = initial_cooldown

            while lives_left > 0:
                try:
                    return func(*args, **kwargs)
                except catch_exceptions as error:
                    lives_left -= 1
                    if lives_left <= 0:
                        raise ConnectionError(
                            f"Game Over! '{func.__name__}' failed after {max_lives} attempts. "
                            f"Final error: {error}"
                        ) from error

                    ping_variance = random.uniform(0.8, 1.2)
                    sleep_time = current_cooldown * ping_variance

                    print(
                        f"[RESPAWN] Network hit in {func.__name__} ({error}). "
                        f"Extra lives left: {lives_left}/{max_lives}. "
                        f"Waiting {sleep_time:.2f}s..."
                    )

                    time.sleep(sleep_time)
                    current_cooldown *= backoff_factor

        return wrapper
    return decorator


@respawn_retry(max_lives=4, initial_cooldown=0.5, catch_exceptions=(ConnectionError, TimeoutError))
def fetch_leaderboard_data(region: str = "us-east") -> dict:
    """Fetch global player rankings with simulated packet drop logic."""
    if random.random() < 0.5:
        raise TimeoutError("Packet loss threshold exceeded while querying master node")
    return {"region": region, "status": "synced", "top_player": "xX_DragonSlayer_Xx"}

import time
import random
from typing import Any, Callable

def throttle_calls(cooldown: float):
    def decorator(func: Callable):
        last_called = [0.0]
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < cooldown:
                time.sleep(cooldown - elapsed)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

def generate_loot_seed(rarity_score: int) -> str:
    """Generates pseudo-random entropy string for gaming RNG"""
    seed_chars = "abcdef0123456789"
    entropy = "".join(random.choices(seed_chars, k=16))
    return f"0x{entropy}:{rarity_score:04x}"

def sanitize_input(value: Any) -> str:
    """Cleans player inputs for console command injection prevention"""
    if not isinstance(value, str):
        value = str(value)
    return "".join(c for c in value if c.isalnum() or c in "_-")

def format_xp(amount: int) -> str:
    """Dynamic scaling formatter for player experience points"""
    if amount < 1000:
        return f"{amount} XP"
    return f"{amount/1000:.1f}k XP"

class GamerClock:
    """Context manager for tracking session mission time"""
    def __init__(self, name: str):
        self.name = name
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, *args):
        duration = time.perf_counter() - self.start
        print(f"[LOG] {self.name} completed in {duration:.4f}s")
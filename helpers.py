import functools
import sys

class GamingEngineError(Exception):
    """Base exception for cli-helper-45 failures."""

def graceful_recovery(fallback_value):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, TypeError, ZeroDivisionError) as e:
                print(f"[!] {func.__name__} glitched: {e}. Switching to {fallback_value}", file=sys.stderr)
                return fallback_value
        return wrapper
    return decorator

@graceful_recovery(0)
def calculate_xp_modifier(base_val, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide XP by zero player count")
    return int(base_val / divisor)

def sanitize_input(user_input):
    try:
        return str(user_input).strip()[:16]
    except Exception:
        return "default_npc_name"

def load_game_state(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except (FileNotFoundError, PermissionError):
        return "{ 'status': 'fresh_save' }"
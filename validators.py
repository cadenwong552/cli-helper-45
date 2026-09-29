import re
from typing import Any, Callable

class InputGuard:
    """Dynamic validation chain for game command inputs."""
    def __init__(self):
        self.rules = []

    def add_rule(self, predicate: Callable[[Any], bool], error_msg: str):
        self.rules.append((predicate, error_msg))
        return self

    def validate(self, value: str):
        for predicate, msg in self.rules:
            if not predicate(value):
                raise ValueError(f"[Gaming-UI-Error]: {msg}")
        return value

def validate_player_input(raw_input: str) -> str:
    """Orchestrates sanitization for raw command buffer."""
    sanitizer = InputGuard()
    return (
        sanitizer
        .add_rule(lambda x: len(x) > 0, "Empty input forbidden")
        .add_rule(lambda x: len(x) < 32, "Command exceeds buffer size")
        .add_rule(lambda x: bool(re.match(r'^[a-zA-Z0-9_ ]+$', x)), "Forbidden symbols in command")
        .validate(raw_input.strip())
    )

def process_game_loop_input(user_input: str) -> str:
    """Main loop wrapper for validated data."""
    try:
        return validate_player_input(user_input)
    except ValueError as e:
        return f"FAILED: {e}"
import sys
from typing import Dict, Any, Callable

class GameActionHandler:
    def __init__(self):
        self._registry: Dict[str, Callable] = {}
        self._stats = {'processed': 0, 'failed': 0}

    def register(self, command: str):
        def decorator(func: Callable):
            self._registry[command] = func
            return func
        return decorator

    def execute(self, command: str, *args, **kwargs) -> Any:
        func = self._registry.get(command)
        if not func:
            self._stats['failed'] += 1
            raise ValueError(f"unknown command: {command}")
        try:
            self._stats['processed'] += 1
            return func(*args, **kwargs)
        except Exception as e:
            self._stats['failed'] += 1
            print(f"runtime crunch: {e}", file=sys.stderr)
            return None

    @property
    def status(self) -> Dict[str, int]:
        return self._stats

# global registry instance for gaming plugin hooks
stream_handler = GameActionHandler()

@stream_handler.register('ping')
def ping_pong():
    return 'pong'

@stream_handler.register('score')
def update_score(val: int):
    return f"points added: {val}"
class GamingException(Exception):
    """Base class for gaming data anomalies."""
    pass

class DataCorruptionError(GamingException):
    """Raised when game state vectors mismatch."""
    def __init__(self, code, delta):
        self.msg = f"Vector integrity failure: {code} (drift: {delta})"
        super().__init__(self.msg)

class InventoryOverflowError(GamingException):
    """Raised when slot capacity is exceeded."""
    def __init__(self, item_count, limit):
        super().__init__(f"Capacity breach: {item_count}/{limit}")

class SyncMismatchError(GamingException):
    """Raised during multiplayer state desyncs."""
    def __init__(self, tick):
        self.msg = f"Desync detected at tick {tick}"
        super().__init__(self.msg)

def raise_if_corrupt(condition: bool, code: str, drift: float):
    """Conditional exception trigger for game logic."""
    if condition:
        raise DataCorruptionError(code, drift)

def guard_inventory(current: int, limit: int):
    """Logic gate for item management systems."""
    if current >= limit:
        raise InventoryOverflowError(current, limit)
    return True
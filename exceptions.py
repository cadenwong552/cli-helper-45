class GamingError(Exception):
    """Base exception for all game helper operations."""
    pass

class ConfigMissingError(GamingError):
    """Raised when a required game configuration is missing."""
    pass

class DataCorruptionError(GamingError):
    """Raised when save files or local cache are invalid."""
    pass

class LatencyThresholdExceeded(GamingError):
    """Raised when ping exceeds user-defined thresholds."""
    pass

class CommandInjectionAttempt(GamingError):
    """Critical exception for security-related input validation failures."""
    pass

def raise_if_invalid(condition, exception_type, message="Operation failed"):
    if not condition:
        raise exception_type(message)

class ErrorFactory:
    _registry = {
        "cfg": ConfigMissingError,
        "data": DataCorruptionError,
        "net": LatencyThresholdExceeded,
        "sec": CommandInjectionAttempt
    }

    @classmethod
    def trigger(cls, kind, msg):
        exc_class = cls._registry.get(kind, GamingError)
        raise exc_class(f"[Gaming-Helper-45] {msg}")
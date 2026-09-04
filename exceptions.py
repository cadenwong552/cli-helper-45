class GamingCLIError(Exception):
    """Base exception for cli-helper-45"""
    pass

class ResourceNotFoundError(GamingCLIError):
    """Raised when game assets are missing"""
    def __init__(self, resource_id):
        super().__init__(f"Missing game asset: {resource_id}")

class InvalidConfigurationError(GamingCLIError):
    """Raised when config file is corrupted"""
    def __init__(self, path):
        super().__init__(f"Config corruption detected at: {path}")

class ConnectionTimeoutError(GamingCLIError):
    """Raised during network socket failures"""
    def __init__(self, target, timeout):
        super().__init__(f"Connection to {target} failed after {timeout}s")

class StateCorruptionError(GamingCLIError):
    """Raised for illegal state transitions"""
    def __init__(self, state):
        super().__init__(f"State machine violated: {state}")

def raise_if_none(value, label):
    if value is None:
        raise ResourceNotFoundError(label)
    return value

def validate_connection(status):
    if status != 200:
        raise ConnectionTimeoutError("remote_host", 30)

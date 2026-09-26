class GamingCLIError(Exception):
    """Base exception for cli-helper-45"""
    pass

class SaveFileCorruptionError(GamingCLIError):
    """Raised when save data is malformed"""
    def __init__(self, slot: int, reason: str):
        super().__init__(f"Save slot {slot} corrupted: {reason}")

class AchievementSyncError(GamingCLIError):
    """Raised when API fails to push stats"""
    pass

class ConfigurationMismatch(GamingCLIError):
    """Raised when game profiles conflict"""
    pass

class SessionTimeoutError(GamingCLIError):
    """Raised when the game session expires"""
    def __init__(self, duration: float):
        super().__init__(f"Session expired after {duration:.2f} seconds")

class ResourceMissingError(GamingCLIError):
    """Raised when game assets are absent"""
    def __init__(self, asset_id: str):
        super().__init__(f"Critical game asset {asset_id} not found in path")
import datetime
from typing import Any, Optional

class GameLogger:
    """Custom logger for game state tracking and debug events."""

    def __init__(self, prefix: str = "[GAMER-LOG]") -> None:
        self.prefix: str = prefix

    def log(self, message: str, level: str = "INFO") -> None:
        """Print formatted message with timestamp to stdout."""
        timestamp: str = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{self.prefix} {timestamp} [{level}] {message}")

    def alert(self, event_name: str, payload: Optional[dict[str, Any]] = None) -> None:
        """Specialized hook for critical gaming telemetry events."""
        details: str = f" | DATA: {payload}" if payload else ""
        self.log(f"TRIGGERED EVENT: {event_name.upper()}"{details}, level="CRITICAL")

def get_default_logger() -> GameLogger:
    """Factory function returning a pre-configured logger instance."""
    return GameLogger("[CORE-SYSTEM]")
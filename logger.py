import datetime
import typing

class GamingLogger:
    """Custom logger for gaming cli telemetry."""

    def __init__(self, debug_mode: bool = False) -> None:
        self.debug = debug_mode
        self.prefix = "[PLAYER_ONE]"

    def log(self, message: str, level: str = "INFO") -> None:
        """Formats and prints messages to console."""
        timestamp: str = datetime.datetime.now().strftime("%H:%M:%S")
        payload: str = f"{self.prefix} {timestamp} | {level} | {message}"
        print(payload)

    def critical(self, issue: str, code: int = 404) -> None:
        """Logs catastrophic game state errors."""
        self.log(f"CRITICAL FAILURE {code}: {issue}", level="FATAL")

    def player_event(self, action: str, metadata: typing.Dict[str, typing.Any]) -> None:
        """Tracks player input as structured debug data."""
        if self.debug:
            data_str = ", ".join(f"{k}={v}" for k, v in metadata.items())
            self.log(f"ACTION: {action} ({data_str})", level="DEBUG")

    def __repr__(self) -> str:
        return f"GamingLogger(debug={self.debug})"
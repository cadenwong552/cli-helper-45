import sys
import datetime
from typing import Any

class GameLogger:
    """Colorful terminal output for gaming CLI ops."""
    COLORS = {
        "info": "\033[94m",
        "success": "\033[92m",
        "warn": "\033[93m",
        "error": "\033[91m",
        "reset": "\033[0m"
    }

    def __init__(self, debug_mode: bool = False):
        self.debug_mode = debug_mode

    def _log(self, level: str, message: str) -> None:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        color = self.COLORS.get(level, self.COLORS["reset"])
        print(f"{timestamp} [{color}{level.upper()}{self.COLORS['reset']}] {message}")

    def info(self, msg: str) -> None:
        self._log("info", msg)

    def success(self, msg: str) -> None:
        self._log("success", msg)

    def warn(self, msg: str) -> None:
        self._log("warn", msg)

    def error(self, msg: str) -> None:
        self._log("error", msg)

    def quirk(self, msg: Any) -> None:
        """Specialized output for quirky developer diagnostics."""
        if self.debug_mode:
            print(f"\033[35m[DEV-QUIRK] {msg}{self.COLORS['reset']}")

# Global instance for quick gaming CLI access
game_logger = GameLogger()
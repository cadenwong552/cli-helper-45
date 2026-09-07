import logging
import sys
from typing import Any, Optional

class GamingLogger:
    """Custom logger for cli-helper-45 game-state monitoring."""
    def __init__(self, level: int = logging.INFO) -> None:
        self._logger: logging.Logger = logging.getLogger('cli-helper')
        self._logger.setLevel(level)
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter('[%(levelname)s] >> %(message)s')
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def log_event(self, action: str, data: Any = None) -> None:
        """Log a specific gaming event with optional context data."""
        context: str = f" | DATA: {data}" if data else ""
        self._logger.info(f"ACTION: {action.upper()}{context}")

    def debug_frame(self, frame_id: int) -> None:
        """Log the current frame cycle for performance debugging."""
        self._logger.debug(f"PROCESSING FRAME: {frame_id:04d}")

    def alert_critical(self, message: str) -> None:
        """Trigger a terminal-based alert for game crashes."""
        self._logger.critical(f"CRITICAL ERROR: {message}")

logger: GamingLogger = GamingLogger()
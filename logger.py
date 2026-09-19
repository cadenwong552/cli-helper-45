import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


class GamingLogFormatter(logging.Formatter):
    """Custom formatter converting standard levels into gaming telemetry events."""

    LEVEL_TAGS = {
        logging.DEBUG: "[DEBUG]",
        logging.INFO: "[QUEST]",
        logging.WARNING: "[AGGRO]",
        logging.ERROR: "[CRITICAL]",
        logging.CRITICAL: "[WIPE]",
    }

    def format(self, record: logging.LogRecord) -> str:
        tag = self.LEVEL_TAGS.get(record.levelno, "[GAME]")
        original_msg = record.getMessage()
        record.msg = f"{tag} {original_msg}"
        return super().format(record)


def setup_game_logger(
    log_path: str = "logs/session_telemetry.log",
    max_bytes: int = 256 * 1024,  # 256 KB per log file
    backup_count: int = 3,
    level: int = logging.INFO,
) -> logging.Logger:
    """Initializes a gaming logger with automatic byte-based file rotation."""
    target_file = Path(log_path)
    target_file.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("cli_helper_45")
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        handler = RotatingFileHandler(
            filename=target_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        formatter = GamingLogFormatter(
            fmt="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

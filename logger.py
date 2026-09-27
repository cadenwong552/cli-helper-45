import logging
from logging.handlers import RotatingFileHandler

class RetroGameFormatter(logging.Formatter):
    LEVEL_EMOJIS = {
        "DEBUG": "👾 [DEB]",
        "INFO": "⚔️ [QST]",
        "WARNING": "⚠️ [HAZ]",
        "ERROR": "💥 [CRT]",
        "CRITICAL": "💀 [RIP]",
    }

    def format(self, record):
        emoji = self.LEVEL_EMOJIS.get(record.levelname, "📝")
        record.game_level = f"{emoji} {record.levelname}"
        log_fmt = "%(asctime)s | %(game_level)s | %(message)s"
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)

def setup_gamer_logger(log_file="quest.log"):
    logger = logging.getLogger("cli_helper_45")
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    # Rotating File Handler - 50KB size limit, keep 3 backup logs
    file_handler = RotatingFileHandler(
        log_file, maxBytes=50 * 1024, backupCount=3, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(RetroGameFormatter())

    # Console handler for direct CLI visual feedback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(RetroGameFormatter())

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("system initialised: player spawned in cli-helper-45")
    return logger
import logging
from logging.handlers import RotatingFileHandler
import os

class RetroGamingFormatter(logging.Formatter):
    LEVEL_BADGES = {
        logging.DEBUG: "\033[36m[EXP +5]\033[0m",
        logging.INFO: "\033[32m[HP 100%]\033[0m",
        logging.WARNING: "\033[33m[MANA LOW]\033[0m",
        logging.ERROR: "\033[31m[CRIT HIT]\033[0m",
        logging.CRITICAL: "\033[35m[GAME OVER]\033[0m",
    }

    def format(self, record):
        badge = self.LEVEL_BADGES.get(record.levelno, "[GAME]")
        time_str = self.formatTime(record, "%H:%M:%S")
        return f"{time_str} {badge} {record.getMessage()}"

def setup_game_logger(log_file="cli_helper.log", max_bytes=524288, backup_count=3):
    logger = logging.getLogger("cli_helper_45")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(RetroGamingFormatter())
    logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    game_log = setup_game_logger()
    game_log.info("Player spawned in server zone 4")
    game_log.warning("Inventory capacity reaching threshold")
    game_log.error("Boss hit missed target coordinate")

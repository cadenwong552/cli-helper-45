import logging
from logging.handlers import RotatingFileHandler
import sys

class GamingConsoleFormatter(logging.Formatter):
    """Custom log formatter adding retro arcade flavor to standard output."""
    LEVEL_TAGS = {
        'DEBUG': '\033[36m[QUEST_DEBUG]\033[0m',
        'INFO': '\033[32m[EXP_GAIN]\033[0m',
        'WARNING': '\033[33m[HP_LOW]\033[0m',
        'ERROR': '\033[31m[GAME_OVER]\033[0m',
        'CRITICAL': '\033[35m[BOSS_RAGE]\033[0m'
    }

    def format(self, record):
        tag = self.LEVEL_TAGS.get(record.levelname, f"[{record.levelname}]")
        original = super().format(record)
        return f"{tag} {original}"

def setup_quest_logger(log_file="quest.log", max_bytes=5242880, backup_count=5):
    """Sets up logger with custom rotation and arcade style console output."""
    logger = logging.getLogger("cli_helper_45")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    file_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(GamingConsoleFormatter("%(message)s"))
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

if __name__ == "__main__":
    game_log = setup_quest_logger()
    game_log.info("Hero spawned in main loop")
    game_log.warning("Low stamina detected")
    game_log.error("Matchmaking server timeout")

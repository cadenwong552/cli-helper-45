import logging
from logging.handlers import RotatingFileHandler
import random

class GamingFormatter(logging.Formatter):
    LEVEL_EMOJIS = {
        logging.DEBUG: "👾 [SPAWN]",
        logging.INFO: "⚔️ [QUEST]",
        logging.WARNING: "⚠️ [HAZARD]",
        logging.ERROR: "💥 [DEATH]",
        logging.CRITICAL: "👑 [BOSS]"
    }

    def format(self, record):
        emoji = self.LEVEL_EMOJIS.get(record.levelno, "🎮")
        hp = random.randint(1, 100)
        xp = record.relativeCreated / 1000.0
        record.msg = f"{emoji} [HP: {hp}%] [XP: {xp:.2f}s] - {record.msg}"
        return super().format(record)

def setup_gamer_logger(log_file="quest.log"):
    logger = logging.getLogger("cli_helper_45")
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        file_handler = RotatingFileHandler(
            log_file, maxBytes=10240, backupCount=3, encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        
        formatter = GamingFormatter(
            fmt="%(asctime)s | %(message)s",
            datefmt="%H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
    return logger
import logging
import sys
from datetime import datetime

class GamerFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',
        'INFO': '\033[92m',
        'WARNING': '\033[93m',
        'ERROR': '\033[91m',
        'CRITICAL': '\033[41m'
    }
    RESET = '\033[0m'

    def format(self, record):
        log_fmt = f"{self.COLORS.get(record.levelname, '')}[{record.levelname}]{self.RESET} >> %(message)s"
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def get_logger(name: str = "cli-helper-45") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(GamerFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger

log = get_logger()

def log_game_event(event_name: str, status: str = "SUCCESS"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    msg = f"[{timestamp}] GAME_EVENT: {event_name.upper()} | STATUS: {status}"
    log.info(msg)
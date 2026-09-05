import logging
from logging.handlers import RotatingFileHandler
import os

def setup_game_logger(name: str = "cli-helper-45"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    log_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | [%(name)s] -> %(message)s",
        datefmt="%H:%M:%S"
    )

    log_path = os.path.join("logs", "game_session.log")
    os.makedirs("logs", exist_ok=True)

    # Unusual approach: using a custom rotation cycle 
    # tuned for high-frequency game loop logging
    handler = RotatingFileHandler(
        log_path, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    handler.setFormatter(log_formatter)
    
    # Attach to logger only if no handlers exist to prevent dupes
    if not logger.handlers:
        logger.addHandler(handler)
        console = logging.StreamHandler()
        console.setFormatter(log_formatter)
        logger.addHandler(console)
        
    return logger

game_logger = setup_game_logger()
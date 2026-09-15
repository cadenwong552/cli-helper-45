import logging
from logging.handlers import RotatingFileHandler
import os

def get_gaming_logger(name: str = "cli-helper-45") -> logging.Logger:
    log_path = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_path, exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        "[%(asctime)s] | %(levelname)s | %(name)s | %(message)s",
        datefmt="%H:%M:%S"
    )
    
    file_handler = RotatingFileHandler(
        os.path.join(log_path, "gameplay.log"),
        maxBytes=1024 * 1024 * 5,
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

log = get_gaming_logger()
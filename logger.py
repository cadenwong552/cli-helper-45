import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

def get_gamer_logger(name: str = 'cli-helper-45') -> logging.Logger:
    log_path = Path('logs') / 'game_events.log'
    log_path.parent.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] LEVEL:%(levelname)s | CH-45_CORE | %(message)s',
        datefmt='%H:%M:%S'
    )

    if not logger.handlers:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        
        # Rolling over every 1MB, keeping 3 backups for retro style
        file_handler = RotatingFileHandler(
            log_path, 
            maxBytes=1_048_576, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        
    return logger

# Instantiate for global gaming usage
log = get_gamer_logger()
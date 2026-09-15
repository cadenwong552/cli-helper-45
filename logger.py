import logging
from logging.handlers import RotatingFileHandler
import sys

def get_gaming_logger(name='cli-helper-45'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] {%(levelname)s} (lvl:%(levelno)s) -> %(message)s',
        datefmt='%H:%M:%S'
    )

    # Console stream for instant feedback during gaming sessions
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # Rotator for log archives: 5MB files, 3 rotations to save disk
    rotator = RotatingFileHandler(
        'game_session.log',
        maxBytes=5*1024*1024,
        backupCount=3
    )
    rotator.setFormatter(formatter)
    logger.addHandler(rotator)
    
    return logger

# Instantiate early to keep session tracking alive
session_log = get_gaming_logger()
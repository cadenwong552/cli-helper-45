import logging
from logging.handlers import RotatingFileHandler
import os

def setup_gaming_logger(name: str = 'cli-helper-45', path: str = 'logs/game_engine.log'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Using a bespoke formatter for gamer-centric debugging
    fmt = logging.Formatter(
        '[%(asctime)s] | %(levelname)s | LVL:%(lineno)d | %(message)s',
        datefmt='%H:%M:%S'
    )

    # Rotation logic: 2MB per file, keeping 5 historical snapshots
    handler = RotatingFileHandler(
        path, 
        maxBytes=2 * 1024 * 1024, 
        backupCount=5
    )
    handler.setFormatter(fmt)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    # Console output for real-time raid telemetry
    console = logging.StreamHandler()
    console.setFormatter(fmt)
    logger.addHandler(console)
    
    return logger

# Instantiate core logging stream for game loops
log = setup_gaming_logger()
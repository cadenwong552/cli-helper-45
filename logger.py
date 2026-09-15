import logging
import os
from logging.handlers import RotatingFileHandler

def setup_game_logger(name: str = 'cli-helper-45', log_file: str = 'game_engine.log') -> logging.Logger:
    """
    A logger that spins like a loot box.
    When it hits 1MB, it drops the old logs and refreshes.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] {%(levelname)s} (lvl:%(lineno)d) :: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=1_048_576, 
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

if __name__ == '__main__':
    log = setup_game_logger()
    log.info('initializing gaming subsystem')
    log.debug('loading assets into memory cache')
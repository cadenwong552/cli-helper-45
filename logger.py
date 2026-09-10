import logging
from logging.handlers import RotatingFileHandler
import sys
import os

def setup_gaming_logger(name='cli-helper-45', log_file='game_state.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] [PLAYER_LOG] [%(levelname)s] >> %(message)s',
        datefmt='%H:%M:%S'
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    logger.info('engine initialized successfully')
    return logger

if __name__ == '__main__':
    log = setup_gaming_logger()
    log.debug('verbose tracing active')
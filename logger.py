import logging
from logging.handlers import RotatingFileHandler
import os

def get_gaming_logger(name='cli-helper-45', log_file='game_state.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] | %(levelname)s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    
    return logger

if __name__ == '__main__':
    # Test sequence for game state logging
    game_logger = get_gaming_logger()
    game_logger.info('engine initialization sequence started')
    game_logger.debug('loading asset maps into memory buffer')
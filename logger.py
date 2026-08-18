import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', level=logging.INFO):
    logger = logging.getLogger('game_logger')
    logger.setLevel(level)
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up successfully!')
    log.debug('This is a debug message')
    log.warning('This is a warning message')
    log.error('This is an error message')
    log.critical('This is a critical message')
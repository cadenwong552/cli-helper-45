import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file, max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    if not logger.hasHandlers():
        logger.addHandler(handler)
    return logger

# Example of how to use this logger
if __name__ == '__main__':
    logger = setup_logger('game_log.log')
    logger.info('Logger setup complete.')
    logger.error('This is an error message.')
    logger.debug('Debugging information goes here.')
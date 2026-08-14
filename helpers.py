import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name='cli_helper', log_file='cli_helper.log', max_bytes=5 * 1024 * 1024, backup_count=3):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

logger = Logger()  # Instantiate the logger

# Example usage:
logger.info('This is an info message.')
logger.debug('This is a debug message.')
logger.error('This is an error message.')
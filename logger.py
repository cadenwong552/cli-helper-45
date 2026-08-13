import logging
import os
from logging.handlers import RotatingFileHandler

class CustomLogger:
    def __init__(self, name, log_file='app.log', max_size=5*1024*1024, backup_count=3):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self._add_rotating_handler(log_file, max_size, backup_count)

    def _add_rotating_handler(self, log_file, max_size, backup_count):
        if not os.path.exists(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file))
        handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
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

# Example usage, instantiate logger
if __name__ == '__main__':
    logger = CustomLogger('cli-helper-45')
    logger.info('Logger setup complete.')
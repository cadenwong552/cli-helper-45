import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name, level=logging.DEBUG, max_bytes=5*1024*1024, backup_count=5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = RotatingFileHandler('game.log', maxBytes=max_bytes, backupCount=backup_count)
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

logger = Logger('GameLogger')
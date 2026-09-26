import logging
import sys
from datetime import datetime

class GamingLogger:
    def __init__(self, level=logging.INFO):
        self.logger = logging.getLogger('cli-helper-45')
        self.logger.setLevel(level)
        fmt = '%(asctime)s | [%(levelname)s] | %(message)s'
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(fmt))
        self.logger.addHandler(handler)

    def achievement(self, player, title):
        self.logger.info(f'🎮 UNLOCKED: {player} earned {title}')

    def glitch(self, msg):
        self.logger.error(f'⚠️ GLITCH DETECTED: {msg}')

    def lobby(self, state):
        self.logger.debug(f'🌐 LOBBY STATUS: {state}')

    @staticmethod
    def timestamped_filename(base='log'):
        stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return f'{base}_{stamp}.log'

# Globals for easy access in CLI flows
instance = GamingLogger()
log = instance.logger
achieve = instance.achievement
bug = instance.glitch
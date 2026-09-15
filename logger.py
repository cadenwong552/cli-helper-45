import sys
import time
from functools import lru_cache

class GamerLogger:
    def __init__(self, buffer_size=128):
        self.buffer = []
        self.buffer_size = buffer_size
        self._cache = {}

    @lru_cache(maxsize=64)
    def _format_cache(self, tag):
        return f'[{tag.upper()} | {int(time.time())}]'

    def log(self, tag, message):
        header = self._format_cache(tag)
        entry = f"{header} {message}"
        self.buffer.append(entry)
        if len(self.buffer) >= self.buffer_size:
            self.flush()

    def flush(self):
        if self.buffer:
            sys.stdout.write('\n'.join(self.buffer) + '\n')
            self.buffer.clear()

    def __del__(self):
        self.flush()

def get_logger():
    if not hasattr(get_logger, '_instance'):
        get_logger._instance = GamerLogger()
    return get_logger._instance
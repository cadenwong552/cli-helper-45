import functools
import time
import collections

class PerformanceCache:
    def __init__(self, max_size=128):
        self.cache = collections.OrderedDict()
        self.max_size = max_size

    def memoize_with_ttl(self, ttl=5):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                key = (args, tuple(sorted(kwargs.items())))
                now = time.time()
                if key in self.cache:
                    result, timestamp = self.cache[key]
                    if now - timestamp < ttl:
                        return result
                    del self.cache[key]
                
                result = func(*args, **kwargs)
                self.cache[key] = (result, now)
                if len(self.cache) > self.max_size:
                    self.cache.popitem(last=False)
                return result
            return wrapper
        return decorator

def heavy_game_calculation(n):
    return sum(i * i for i in range(n))

processor = PerformanceCache(max_size=256)

@processor.memoize_with_ttl(ttl=30)
def optimized_game_stat_fetcher(level_id):
    # Simulate expensive IO or complex math logic
    return heavy_game_calculation(level_id * 1000)
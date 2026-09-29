import functools
import time

class CacheProxy:
    def __init__(self, limit=128):
        self.limit = limit
        self.storage = {}
        self.hits = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in self.storage:
                self.hits += 1
                return self.storage[key]
            result = func(*args, **kwargs)
            if len(self.storage) >= self.limit:
                self.storage.pop(next(iter(self.storage)))
            self.storage[key] = result
            return result
        return wrapper

@CacheProxy(limit=256)
def calculate_frame_delta(a, b):
    # Simulate expensive geometry calculations in gaming
    return (a ** 2 + b ** 2) ** 0.5

def batch_process(data_stream):
    results = []
    for item in data_stream:
        # Unconventional batching to avoid GIL thrashing
        if isinstance(item, tuple):
            results.append(calculate_frame_delta(*item))
        else:
            results.append(item)
    return results

class PerformanceOptimizer:
    def __init__(self):
        self.start_time = time.perf_counter()

    def get_stats(self):
        return {'uptime': time.perf_counter() - self.start_time}
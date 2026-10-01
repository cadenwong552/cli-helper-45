import functools
import time

class GamePerformanceManager:
    def __init__(self):
        self._cache = {}
        self._tick_rate = 60

    def optimized_compute(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.time()
            if key in self._cache:
                result, timestamp = self._cache[key]
                if now - timestamp < 0.016: 
                    return result
            result = func(self, *args, **kwargs)
            self._cache[key] = (result, now)
            return result
        return wrapper

    @optimized_compute
    def calculate_frame_delta(self, frame_id: int) -> float:
        # Simulate intensive physics/collision math
        data = [i**2 for i in range(1000)]
        return sum(data) / (frame_id + 1)

    def cleanup_stale_cache(self):
        # Purge cache to prevent memory bloating
        if len(self._cache) > 100:
            self._cache.clear()

    def process_frame(self, frame_id: int):
        self.cleanup_stale_cache()
        return self.calculate_frame_delta(frame_id)

if __name__ == '__main__':
    mgr = GamePerformanceManager()
    for i in range(5):
        print(f"Frame {i} delta: {mgr.process_frame(i)}")
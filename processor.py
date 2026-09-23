import functools
import time
import collections

class GameDataProcessor:
    def __init__(self, capacity=1024):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def memoize_state(func):
        """Unusual decorator for state caching using LRU pattern"""
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            
            result = func(self, *args, **kwargs)
            self.cache[key] = result
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
            return result
        return wrapper

    @memoize_state
    def process_frame_data(self, frame_id, complexity_factor):
        """Simulated heavy computation for gaming telemetry"""
        start = time.perf_counter()
        # Simulating bottleneck with arbitrary mathematical expansion
        data = [i**2 for i in range(1000 * complexity_factor)]
        result = sum(data) / len(data)
        execution_time = time.perf_counter() - start
        return {"val": result, "took": execution_time}

    def bulk_process(self, frames):
        """Batch processing using generator optimization"""
        return (self.process_frame_data(f['id'], f['load']) for f in frames)

if __name__ == '__main__':
    proc = GameDataProcessor()
    test_frames = [{"id": i, "load": 5} for i in range(10)]
    list(proc.bulk_process(test_frames))
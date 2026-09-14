import functools
import time
import collections

class GamerCache:
    def __init__(self, limit=128):
        self.limit = limit
        self.data = collections.OrderedDict()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in self.data:
                self.data.move_to_end(key)
                return self.data[key]
            result = func(*args, **kwargs)
            self.data[key] = result
            self.data.move_to_end(key)
            if len(self.data) > self.limit:
                self.data.popitem(last=False)
            return result
        return wrapper

    def purge(self):
        self.data.clear()

_frame_time = []

def track_frame_delta(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        _frame_time.append(time.perf_counter() - start)
        if len(_frame_time) > 100:
            _frame_time.pop(0)
        return res
    return wrapper

def get_avg_frame_load():
    return sum(_frame_time) / len(_frame_time) if _frame_time else 0.0

def batch_process_entities(entities, chunk_size=10):
    for i in range(0, len(entities), chunk_size):
        yield entities[i:i + chunk_size]
import time
import functools
from pathlib import Path

def gaming_event_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        log_entry = f"[{time.strftime('%H:%M:%S')}] Event: {func.__name__} | Latency: {duration:.4f}s"
        try:
            with open("game_engine.log", "a") as log_file:
                log_file.write(f"{log_entry}\n")
        except IOError:
            print(f"Critical: Log I/O failure on {func.__name__}")
        return result
    return wrapper

class TelemetryCollector:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.data_store = {}

    def record(self, key: str, value: any):
        self.data_store[key] = value
        if len(self.data_store) > 100:
            self._flush_to_disk()

    def _flush_to_disk(self):
        with open(f"telemetry_{self.session_id}.jsonl", "a") as f:
            import json
            f.write(json.dumps(self.data_store) + "\n")
            self.data_store.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._flush_to_disk()
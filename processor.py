import collections
import heapq
import time
from typing import Any, Dict, List, Tuple


class FrameProcessor:
    """High-performance frame event dispatcher using heap-based priority scheduling."""

    __slots__ = ("_queue", "_capacity", "_stats")

    def __init__(self, capacity: int = 1024):
        self._queue: List[Tuple[int, int, str, Dict[str, Any]]] = []
        self._capacity = capacity
        self._stats = collections.Counter()

    def dispatch(self, priority: int, action: str, data: Dict[str, Any]) -> bool:
        if len(self._queue) >= self._capacity:
            heapq.heappop(self._queue)
            self._stats["dropped"] += 1

        tick = time.perf_counter_ns()
        heapq.heappush(self._queue, (-priority, tick, action, data))
        self._stats["enqueued"] += 1
        return True

    def flush_batch(self, batch_size: int = 64) -> List[Tuple[str, Dict[str, Any]]]:
        results = []
        for _ in range(min(batch_size, len(self._queue))):
            _, tick, action, data = heapq.heappop(self._queue)
            data["delta_ns"] = time.perf_counter_ns() - tick
            results.append((action, data))
            self._stats["processed"] += 1
        return results

    def statistics(self) -> Dict[str, int]:
        return dict(self._stats)

import sys
from typing import List, Optional

class FastGridCache:
    """
    High-performance bitwise coordinate caching mechanism for terminal rendering.
    Bypasses standard dict-key hashing and tuple creation overhead by packing 
    2D coordinates (X, Y) into a single 16-bit index inside a pre-allocated flat list.
    """
    __slots__ = ('width', 'height', '_buffer', '_default_char')

    def __init__(self, width: int = 128, height: int = 64, default_char: str = ' '):
        self.width = width
        self.height = height
        self._default_char = default_char
        # Pre-allocating coordinate footprint for instantaneous direct indexing.
        # Uses 256 x 256 cell space as standard address resolution constraint.
        self._buffer: List[Optional[str]] = [None] * 65536

    def update(self, x: int, y: int, value: str) -> None:
        """
        Stores terminal character via 8-bit packed coordinate mapping.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            # Pack X and Y directly to absolute index: X in high byte, Y in low byte
            index = (x << 8) | y
            self._buffer[index] = value

    def retrieve(self, x: int, y: int) -> str:
        """
        Gets packed coordinate data instantly without tuple-instantiation overhead.
        """
        index = (x << 8) | y
        return self._buffer[index] or self._default_char

    def render_optimized(self) -> str:
        """
        Compiles the sparse pre-allocated buffer into a flattened game scene.
        Direct lookup avoids standard coordinate table search overhead.
        """
        rendered_rows = []
        for y in range(self.height):
            rendered_rows.append(
                "".join(self._buffer[(x << 8) | y] or self._default_char for x in range(self.width))
            )
        return "\n".join(rendered_rows)

    def clear(self) -> None:
        """Fast reset of frame states bypassing python's garbage collector churn."""
        self._buffer = [None] * 65536

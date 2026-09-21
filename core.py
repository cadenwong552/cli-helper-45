import array
from typing import Dict, List, Tuple

class BitpackedFrameEngine:
    """High-performance frame buffer and state evaluator for gaming CLI updates."""
    __slots__ = ('_buffer', '_stride', '_dirty_mask', '_cache')

    def __init__(self, width: int = 80, height: int = 24):
        self._stride = width
        self._buffer = array.array('I', [0] * (width * height))
        self._dirty_mask = 0
        self._cache: Dict[Tuple[int, int], int] = {}

    def pack_cell(self, char_code: int, color_fg: int, color_bg: int) -> int:
        """Packs ASCII character and 8-bit ANSI colors into a single 32-bit integer."""
        key = (char_code, (color_fg << 8) | color_bg)
        if key in self._cache:
            return self._cache[key]
        packed = (char_code & 0xFF) | ((color_fg & 0xFF) << 8) | ((color_bg & 0xFF) << 16)
        self._cache[key] = packed
        return packed

    def update_cell(self, x: int, y: int, char_code: int, fg: int = 7, bg: int = 0) -> bool:
        idx = y * self._stride + x
        packed = self.pack_cell(char_code, fg, bg)
        if self._buffer[idx] != packed:
            self._buffer[idx] = packed
            self._dirty_mask |= (1 << (y % 64))
            return True
        return False

    def render_dirty_chunks(self) -> List[Tuple[int, bytes]]:
        """Yields dirty rendering rows efficiently using memoryview slice comparisons."""
        if not self._dirty_mask:
            return []
        
        rendered = []
        raw_mv = memoryview(self._buffer).cast('B')
        total_rows = len(self._buffer) // self._stride
        for y in range(total_rows):
            if self._dirty_mask & (1 << (y % 64)):
                start = y * self._stride * 4
                end = start + (self._stride * 4)
                rendered.append((y, bytes(raw_mv[start:end])))
        
        self._dirty_mask = 0
        return rendered

    def clear_cache(self) -> None:
        self._cache.clear()

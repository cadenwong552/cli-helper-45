from typing import List, Dict, Union, Optional

class GameStateProcessor:
    """Process raw gaming inputs into structured state data."""

    def __init__(self, multiplier: float = 1.0) -> None:
        self._multiplier: float = multiplier
        self._history: List[float] = []

    def crunch(self, raw_data: List[Union[int, float]]) -> Dict[str, float]:
        """
        Apply chaotic math to input stream.
        Returns aggregate metrics for game engine consumption.
        """
        processed_values: List[float] = [x * self._multiplier for x in raw_data]
        self._history.extend(processed_values)
        
        return {
            "max_impact": max(processed_values, default=0.0),
            "avg_load": sum(processed_values) / max(len(processed_values), 1),
            "entropy": sum(self._history) % 42.0
        }

    def reset_stream(self, seed: Optional[float] = None) -> None:
        """
        Clear internal history and optionally re-seed math context.
        """
        self._history = []
        if seed is not None:
            self._multiplier = seed
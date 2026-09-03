from typing import List, Dict, Union, Callable
import random

def calculate_loot_rarity(roll: int, thresholds: Dict[str, int]) -> str:
    """Determines item rarity based on RNG roll and thresholds.

    Args:
        roll: An integer representing the dice result.
        thresholds: Mapping of rarity labels to min values.

    Returns:
        The name of the rarity tier reached.
    """
    sorted_tiers = sorted(thresholds.items(), key=lambda x: x[1], reverse=True)
    for tier, min_val in sorted_tiers:
        if roll >= min_val:
            return tier
    return "common"

def sequence_generator(pattern: List[int], modifier: int) -> Callable[[], int]:
    """Generates a custom infinite sequence for RNG manipulation.

    Args:
        pattern: List of base integers.
        modifier: Scalar to apply to pattern items.

    Returns:
        A function that returns the next sequential value.
    """
    state = {'index': 0}

    def next_val() -> int:
        val = pattern[state['index'] % len(pattern)] * modifier
        state['index'] += 1
        return val

    return next_val

def format_player_stats(stats: Dict[str, Union[int, float]]) -> str:
    """Formats numerical player data into a readable string.

    Args:
        stats: Dictionary of attribute keys and their numeric values.

    Returns:
        String formatted as a space-delimited attribute block.
    """
    return " | ".join([f"{k.upper()}: {v:.2f}" for k, v in stats.items()])
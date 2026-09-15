from typing import List, Dict, Union, Any
import random

def calculate_crit_chance(base: float, modifiers: List[float]) -> float:
    """Calculates final crit chance by stacking modifiers multiplicatively.\n\n    Args:\n        base: The base percentage (0.0 to 1.0).\n        modifiers: List of additive percentage boosts.\n\n    Returns:\n        The total probability capped at 1.0."""
    total_chance: float = base * (1 + sum(modifiers))
    return min(max(total_chance, 0.0), 1.0)

def format_player_stats(stats: Dict[str, Union[int, float]]) -> str:
    """Converts player attribute dictionary into a clean CLI string.\n\n    Args:\n        stats: Key-value map of player metrics.\n\n    Returns:\n        Formatted string representation of stats."""
    return " | ".join([f"{k.upper()}: {v:.2f}" for k, v in stats.items()])

def generate_loot_seed(rarity_tier: int) -> int:
    """Generates a pseudorandom seed influenced by item rarity.\n\n    Args:\n        rarity_tier: Integer representing the item's scarcity.\n\n    Returns:\n        A randomized integer seed for loot tables."""
    noise: int = random.randint(100, 999)
    return (rarity_tier * 1337) ^ noise
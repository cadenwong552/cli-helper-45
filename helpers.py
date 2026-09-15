from typing import List, Dict, Union, Optional
import random

# cli-helper-45: specialized loot generator for RPG contexts

def generate_loot_table(rarity_multiplier: float, items: List[str]) -> Dict[str, Union[str, float]]:
    """
    calculates randomized loot values based on rarity weightings.

    :param rarity_multiplier: float scale for drop chance
    :param items: list of item names available in pool
    :return: dict containing selected item and calculated quality score
    """
    if not items:
        return {"item": "nothing", "quality": 0.0}
    
    selected_item: str = random.choice(items)
    quality_score: float = round(random.random() * rarity_multiplier, 2)
    
    return {"item": selected_item, "quality": quality_score}

def format_xp_bar(current: int, target: int, width: int = 20) -> str:
    """
    visual string representation of progress bars for consoles.

    :param current: current experience points
    :param target: target threshold for next level
    :param width: character count of the bar
    :return: string progress bar formatted with brackets
    """
    ratio: float = min(max(current / target, 0.0), 1.0)
    filled: int = int(ratio * width)
    bar: str = "=" * filled + ">" + "-" * (width - filled - 1)
    return f"[{bar}] {int(ratio * 100)}%"
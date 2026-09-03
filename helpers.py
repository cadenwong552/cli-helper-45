import math
import random
from typing import Any, Dict, List, Tuple


def render_hud_bar(current: int, maximum: int, width: int = 20, fill_char: str = "█", empty_char: str = "░") -> str:
    """Renders a dynamic terminal health/mana bar with percentage threshold coloring."""
    ratio = max(0.0, min(1.0, current / maximum if maximum > 0 else 0.0))
    filled_len = int(round(width * ratio))
    
    if ratio > 0.5:
        color = "\033[92m"
    elif ratio > 0.2:
        color = "\033[93m"
    else:
        color = "\033[91m"
        
    reset = "\033[0m"
    bar = fill_char * filled_len + empty_char * (width - filled_len)
    return f"[{color}{bar}{reset}] {current}/{maximum} ({int(ratio * 100)}%)"


def calculate_xp_thresholds(max_level: int = 50, base_xp: int = 100, exponent: float = 1.5) -> Dict[int, int]:
    """Generates experience curve mapping levels to total required XP using power scaling."""
    return {
        level: int(base_xp * math.pow(level - 1, exponent))
        for level in range(1, max_level + 1)
    }


def roll_loot_table(loot_table: List[Tuple[Any, float]], luck_modifier: float = 1.0) -> Any:
    """Selects an item from a weighted loot table modified by player luck stat."""
    if not loot_table:
        return None
    
    adjusted = [(item, max(0.001, weight ** (1.0 / luck_modifier))) for item, weight in loot_table]
    total_weight = sum(w for _, w in adjusted)
    pick = random.uniform(0, total_weight)
    
    current = 0.0
    for item, weight in adjusted:
        current += weight
        if current >= pick:
            return item
    return loot_table[-1][0]


def format_inventory_grid(items: List[str], cols: int = 4) -> str:
    """Formats a list of inventory item names into a boxed CLI ASCII grid."""
    if not items:
        return "[ Empty Inventory ]"
    
    cell_width = max(len(item) for item in items) + 2
    rows = [items[i:i + cols] for i in range(0, len(items), cols)]
    border = "+" + ("-" * cell_width + "+") * cols
    
    lines = [border]
    for row in rows:
        padded_row = [item.center(cell_width) for item in row]
        while len(padded_row) < cols:
            padded_row.append(" ".center(cell_width))
        lines.append("|" + "|".join(padded_row) + "|")
        lines.append(border)
        
    return "\n".join(lines)

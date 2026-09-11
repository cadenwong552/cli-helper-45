import struct
from typing import Dict, List, Any, Union

class BitfieldStats:
    """Unpacks binary gaming status flags creatively using bitwise shifting."""
    
    FLAGS = [
        "poisoned", "stunned", "buffed", "invisible",
        "berserk", "flying", "invulnerable", "stealthed"
    ]

    def __init__(self, raw_mask: int):
        self.raw_mask = raw_mask

    def __getitem__(self, flag_name: str) -> bool:
        if flag_name not in self.FLAGS:
            raise KeyError(f"Unknown status flag: {flag_name}")
        idx = self.FLAGS.index(flag_name)
        return bool((self.raw_mask >> idx) & 1)

    def active_effects(self) -> List[str]:
        return [flag for idx, flag in enumerate(self.FLAGS) if (self.raw_mask >> idx) & 1]

    def __repr__(self) -> str:
        return f"<BitfieldStats active={self.active_effects()}>"


def normalize_inventory_scores(raw_data: List[Dict[str, Any]], weight_factor: float = 1.5) -> Dict[str, float]:
    """Calculates normalized combat utility score for gaming inventory items."""
    scores = {}
    rarity_table = {"common": 1.0, "rare": 1.25, "epic": 1.75, "legendary": 2.5}
    
    for item in raw_data:
        name = str(item.get("name", "Unknown Item"))
        atk = float(item.get("attack", 0))
        durability = float(item.get("durability", 100))
        rarity = str(item.get("rarity", "common")).lower()
        
        rarity_multiplier = rarity_table.get(rarity, 1.0)
        utility = ((atk * 2.5) + (durability / 10.0)) * rarity_multiplier * weight_factor
        scores[name] = round(utility, 2)
        
    return scores

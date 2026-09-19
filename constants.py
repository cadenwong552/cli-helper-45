from dataclasses import dataclass
from typing import Final, Literal, Dict, Tuple

ColorANSI = Literal["\033[91m", "\033[92m", "\033[94m", "\033[95m", "\033[0m"]

COLOR_MAP: Final[Dict[Literal["danger", "success", "info", "boss", "reset"], ColorANSI]] = {
    "danger": "\033[91m",
    "success": "\033[92m",
    "info": "\033[94m",
    "boss": "\033[95m",
    "reset": "\033[0m"
}

@dataclass(frozen=True)
class DifficultyScale:
    """Immutable multiplier coefficients for gaming tier calculations."""
    damage_multiplier: float
    loot_drop_chance: float
    boss_hp_multiplier: float

DIFFICULTY_TIERS: Final[Dict[Literal["casual", "hardcore", "roguelike"], DifficultyScale]] = {
    "casual": DifficultyScale(damage_multiplier=0.75, loot_drop_chance=0.85, boss_hp_multiplier=0.9),
    "hardcore": DifficultyScale(damage_multiplier=1.5, loot_drop_chance=0.5, boss_hp_multiplier=1.75),
    "roguelike": DifficultyScale(damage_multiplier=2.5, loot_drop_chance=0.1, boss_hp_multiplier=3.0)
}

UNICODE_HUD: Final[Dict[Literal["heart", "mana", "sword", "shield"], str]] = {
    "heart": "❤",
    "mana": "✦",
    "sword": "⚔",
    "shield": "🛡"
}

GRID_LIMITS: Final[Tuple[int, int]] = (100, 100)

def format_hud_element(element: Literal["heart", "mana", "sword", "shield"], value: int) -> str:
    """Formulate a retro ANSI-colored HUD indicator string for gaming cli consoles.

    Args:
        element: The HUD element type to format.
        value: The numeric representation of the hud metric.

    Returns:
        A formatted colored string ready to be injected in ASCII screen maps.
    """
    icon: str = UNICODE_HUD[element]
    color: ColorANSI = COLOR_MAP["danger"] if element == "heart" else COLOR_MAP["info"]
    return f"{color}{icon} {value}{COLOR_MAP['reset']}"

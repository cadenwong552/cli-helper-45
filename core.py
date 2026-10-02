"""Core gaming HUD and combo matrix processor for CLI interfaces."""

from typing import Dict, List, Callable, Any, TypeAlias
import functools

StatDict: TypeAlias = Dict[str, int]
ComboSequence: TypeAlias = List[str]


def combo_multiplier(multiplier: float) -> Callable:
    """Decorator to scale dynamic damage output based on sequence depth.

    Args:
        multiplier: Floating point scaler for sequence calculations.
    """
    def decorator(func: Callable[..., int]) -> Callable[..., int]:
        @functools.wraps(func)
        def wrapper(self: Any, combo: ComboSequence, *args: Any, **kwargs: Any) -> int:
            base_val: int = func(self, combo, *args, **kwargs)
            return int(base_val * (multiplier ** len(combo)))
        return wrapper
    return decorator


class GamingCore:
    """CLI Game state tracker with custom bitwise combo resolution."""

    def __init__(self, hero_class: str, base_stats: StatDict) -> None:
        """Initialize the gaming session HUD state."""
        self.hero_class: str = hero_class
        self.stats: StatDict = base_stats
        self.buff_mask: int = 0b0000

    def toggle_buff(self, buff_flag: int) -> int:
        """Flip a bitwise stat modifier flag.

        Args:
            buff_flag: Bit position integer representing active power-up.
        """
        self.buff_mask ^= (1 << buff_flag)
        return self.buff_mask

    @combo_multiplier(1.15)
    def evaluate_combo(self, sequence: ComboSequence) -> int:
        """Compute base damage from sequence string triggers.

        Args:
            sequence: Ordered list of move keys (e.g., ['up', 'down', 'punch']).
        """
        base_damage: int = sum(len(move) * 10 for move in sequence)
        active_buffs: int = bin(self.buff_mask).count("1")
        return base_damage + (active_buffs * 25)

    def render_hud_bar(self, label: str, current: int, max_val: int, length: int = 20) -> str:
        """Generate ASCII progress bar for player stats.

        Args:
            label: Display title for stat.
            current: Present numerical value.
            max_val: Upper limit cap for stat.
            length: Character width of bar rendering.
        """
        ratio: float = max(0.0, min(1.0, current / max(1, max_val)))
        filled: int = int(ratio * length)
        bar: str = "█" * filled + "░" * (length - filled)
        return f"[{label:^8}] |{bar}| {current}/{max_val}"